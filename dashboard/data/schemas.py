"""
Esquemas de dados para o dashboard Maiketeiro
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List
from enum import Enum


class VideoStatus(Enum):
    """Status do processamento de vídeo"""
    PENDING = "Pendente"
    PROCESSING = "Processando"
    COMPLETED = "Concluído"
    FAILED = "Falhou"
    QUEUED = "Na Fila"


class TaskType(Enum):
    """Tipos de tarefas de processamento"""
    TRANSCODE = "Transcodificação"
    CUT = "Corte"
    TRANSCRIPTION = "Transcrição"
    SUBTITLE = "Legenda"
    THUMBNAIL = "Thumbnail"
    COMPRESS = "Compressão"


@dataclass
class Video:
    """Modelo de dados para vídeos"""
    id: str
    title: str
    filename: str
    duration: int  # em segundos
    size_mb: float
    format: str
    resolution: str
    codec: str
    fps: int
    status: VideoStatus
    created_at: datetime
    processed_at: Optional[datetime]
    thumbnail_url: Optional[str]
    transcription: Optional[str]
    subtitle_url: Optional[str]
    tags: List[str]


@dataclass
class Task:
    """Modelo de dados para tarefas de processamento"""
    id: str
    video_id: str
    video_title: str
    task_type: TaskType
    status: VideoStatus
    progress: int  # 0-100
    created_at: datetime
    started_at: Optional[datetime]
    completed_at: Optional[datetime]
    error_message: Optional[str]
    duration_seconds: Optional[float]
    output_file: Optional[str]


@dataclass
class Metric:
    """Modelo de dados para métricas"""
    date: datetime
    videos_processed: int
    total_duration_hours: float
    tasks_completed: int
    tasks_failed: int
    storage_used_gb: float
    avg_processing_time_min: float
