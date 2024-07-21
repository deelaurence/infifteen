import json
import os
import random
from django.core.management.base import BaseCommand
from contribute.models import Question

class Command(BaseCommand):
    help = 'Seed the database with technical questions'

    def handle(self, *args, **options):
        # Question.objects.all().delete()
        # Define the path to the JSON file
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        # json_file_path = os.path.join(base_dir, 'json', 'javascript.json')
        # json_file_path = os.path.join(base_dir, 'json', 'sql.json')
        # json_file_path = os.path.join(base_dir, 'json', 'react.json')
        # json_file_path = os.path.join(base_dir, 'json', 'laravel.json')
        # json_file_path = os.path.join(base_dir, 'json', 'springboot.json')
        # json_file_path = os.path.join(base_dir, 'json', 'django.json')
        json_file_path = os.path.join(base_dir, 'json', 'flutter.json')

        # Ensure the path is correct by printing it
        self.stdout.write(self.style.WARNING(f'Loading questions from {json_file_path}'))

        # Load the questions from the JSON file
        try:
            with open(json_file_path, 'r') as file:
                questions = json.load(file)
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'File not found: {json_file_path}'))
            return

        
        # Seed the database with questions
        for i in range(len(questions)):  # Adjust the range for the number of questions
            question = random.choice(questions)
            Question.objects.create(
                question_text=question['question_text'],
                optionA=question['optionA'],
                optionB=question['optionB'],
                optionC=question.get('optionC', ''),
                optionD=question.get('optionD', ''),
                answer=question['answer'],
                category=question['category'],
                publish=True,
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with questions'))
