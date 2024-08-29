from fastapi import APIRouter


habbit_router = APIRouter(tags=["Habit"])


@habbit_router.get("users/{user_id}/habits/{habit_id}/")
async def get_habit_list(): ...
