class MockDataService:
    '''
        get recommended courses for the login user
        @param username: user's signup email address
    '''

    def getWorkOutRecommendation(self, username):
        # plan_id, plan_name, description, difficulty_level, goal, equipment, training_part
        return [
            {
                "id": 1,
                "name": "Full Body Workout",
                "description": "This workout targets all major muscle groups in the body.",
                "difficulty_level": "Beginner",
                "goal": "Lose Weight",
                "equipment": None,
                "training_part": "Full Body",
            },
            {
                "id": 2,
                "name": "Upper Body Workout",
                "description": "This workout targets the muscles in the upper body.",
                "difficulty_level": "Intermediate",
                "goal": "Build Muscle",
                "equipment": "Dumbbell",
                "training_part": "Upper Body",
            },
            {
                "id": 4,
                "name": "Core Workout",
                "description": "This workout targets the muscles in the core.",
                "difficulty_level": "Beginner",
                "goal": "Tone Muscle",
                "equipment": None,
                "training_part": "Core",
            },
            {
                "id": 6,
                "name": "5K Training",
                "description": "This plan is designed for individuals who want to train for a 5K race.",
                "difficulty_level": "Intermediate",
                "goal": "Run a 5K",
                "equipment": "Treadmill",
                "training_part": "Cardio",
            },
        ]

    '''
        get in progress courses for the login user
        @param username: user's signup email address
    '''

    def getInProgressCourses(self, username):
        return [
            {
                "id": 1,
                "name": "Full Body Workout",
                "description": "This workout targets all major muscle groups in the body.",
                "difficulty_level": "Beginner",
                "goal": "Lose Weight",
                "equipment": None,
                "training_part": "Full Body",
            },
            {
                "id": 2,
                "name": "Upper Body Workout",
                "description": "This workout targets the muscles in the upper body.",
                "difficulty_level": "Intermediate",
                "goal": "Build Muscle",
                "equipment": "Dumbbell",
                "training_part": "Upper Body",
            }
        ]

    def getCourseDetailById(self, couse_id):
        return {
            "id": 1,
            "name": "Full Body Workout",
            "description": "This workout targets all major muscle groups in the body.",
            "difficulty_level": "Beginner",
            "goal": "Lose Weight",
            "equipment": None,
            "training_part": "Full Body",
            "in_progress": True,
        }