# Generated by Django 3.1.7 on 2021-02-25 13:35

from math import ceil

from django.db import migrations

from ..defaults import DAY, HOUR, MINUTE, MONTH, TIME_UNITS, WEEK


def populate_effort(apps, schema_editor):
    """
    Populate the "effort" field by crossing information that
    we have from "duration" and "effort_deprecated" fields
    """
    Course = apps.get_model("courses", "Course")

    TIME_UNITS_IN_SECONDS = {
        MINUTE: 60,
        HOUR: 60 * 60,
        DAY: 24 * 60 * 60,
        WEEK: 7 * 24 * 60 * 60,
        MONTH: 30 * 24 * 60 * 60,
    }

    for course in Course.objects.iterator():
        if course.duration is not None and course.effort_deprecated is not None:
            (duration, duration_unit) = course.duration
            (
                effort_deprecated,
                effort_deprecated_unit,
                effort_deprecated_reference_unit,
            ) = course.effort_deprecated
            duration_in_seconds = duration * TIME_UNITS_IN_SECONDS[duration_unit]
            effort_in_seconds = int(
                (
                    effort_deprecated
                    / TIME_UNITS_IN_SECONDS[effort_deprecated_reference_unit]
                )
                * duration_in_seconds
                * TIME_UNITS_IN_SECONDS[effort_deprecated_unit]
            )

            if effort_in_seconds > TIME_UNITS_IN_SECONDS[HOUR]:
                new_effort = (
                    ceil(effort_in_seconds / TIME_UNITS_IN_SECONDS[HOUR]),
                    HOUR,
                )
            else:
                new_effort = (
                    ceil(effort_in_seconds / TIME_UNITS_IN_SECONDS[MINUTE]),
                    MINUTE,
                )

            course.effort = new_effort
            course.save()


def reverse_populate_effort(apps, schema_editor):
    """
    Rollback to old effort field values

    As new pace course is the old effort field meaning,
    we try to compute course pace and set to effort_deprecated field.
    """
    Course = apps.get_model("courses", "Course")

    for course in Course.objects.iterator():
        if course.effort is not None and course.duration is not None:
            (effort, effort_unit) = course.effort
            (duration, duration_unit) = course.duration

            # Ensure that units are compatible with EffortField requirement
            time_units_keys = list(dict(TIME_UNITS))
            if time_units_keys.index(effort_unit) < time_units_keys.index(
                duration_unit
            ):
                pace = int(effort / duration)
                course.effort_deprecated = (pace, effort_unit, duration_unit)
                course.save()


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0029_auto_20210225_1429"),
    ]

    operations = [
        migrations.RunPython(populate_effort, reverse_populate_effort),
        migrations.RemoveField(model_name="course", name="effort_deprecated"),
    ]
