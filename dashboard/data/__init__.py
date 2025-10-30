"""
Módulo de dados do dashboard Maiketeiro
"""
from .schemas import Video, Task, Metric, VideoStatus, TaskType
from .mock_data import (
    MockDataGenerator,
    get_mock_videos,
    get_mock_tasks,
    get_mock_metrics
)

__all__ = [
    'Video',
    'Task',
    'Metric',
    'VideoStatus',
    'TaskType',
    'MockDataGenerator',
    'get_mock_videos',
    'get_mock_tasks',
    'get_mock_metrics'
]
