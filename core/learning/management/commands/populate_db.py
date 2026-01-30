from django.core.management.base import BaseCommand
from learning.models import User, Course, Module, Enrollment
import random


class Command(BaseCommand):
    help = "Populate database with sample data"

    def handle(self, *args, **kwargs):
        self.stdout.write("Clearing old data...")

        Enrollment.objects.all().delete()
        Module.objects.all().delete()
        Course.objects.all().delete()
        User.objects.exclude(is_superuser=True).delete()

        instructors_data = [
            {"name": "Aman", "email": "aman@course.com"},
            {"name": "Rohit", "email": "rohit@course.com"},
        ]

        students_data = [
            {"name": "Jatin", "email": "jatin@course.com"},
            {"name": "Rahul", "email": "rahul@course.com"},
            {"name": "Sneha", "email": "sneha@course.com"},
            {"name": "Pooja", "email": "pooja@course.com"},
        ]

        instructors = []
        students = []

        for data in instructors_data:
            user = User.objects.create_user(
                username=data["email"].split("@")[0],
                email=data["email"],
                full_name=data["name"],
                password="password123",
                role=User.StatusChoice.INSTRUCTOR,
                is_staff=True,
            )
            instructors.append(user)

        for data in students_data:
            user = User.objects.create_user(
                username=data["email"].split("@")[0],
                email=data["email"],
                full_name=data["name"],
                password="password123",
                role=User.StatusChoice.STUDENT,
            )
            students.append(user)

        course_titles = [
            "Python Basics",
            "Django Development",
            "REST API with DRF",
        ]

        courses = []

        for title in course_titles:
            course = Course.objects.create(
                title=title,
                description=f"Complete course on {title}",
                created_by=random.choice(instructors),
            )
            courses.append(course)

            for i in range(1, 4):
                Module.objects.create(
                    course=course,
                    title=f"{title} - Module {i}",
                    duration_minutes=random.randint(30, 120),
                )

        for student in students:
            selected_courses = random.sample(courses, k=random.randint(1, 2))
            for course in selected_courses:
                Enrollment.objects.create(
                    student=student,
                    course=course,
                    status=random.choice(
                        [
                            Enrollment.StatusChoice.ACTIVE,
                            Enrollment.StatusChoice.COMPLETED,
                        ]
                    ),
                )

        self.stdout.write(self.style.SUCCESS("Database populated successfully"))
