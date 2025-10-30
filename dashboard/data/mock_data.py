"""
Gerador de dados mockados para o dashboard Maiketeiro
"""
import random
from datetime import datetime, timedelta
from typing import List
import pandas as pd
from faker import Faker

from .schemas import Video, Task, Metric, VideoStatus, TaskType

fake = Faker('pt_BR')


class MockDataGenerator:
    """Gerador de dados mockados para desenvolvimento e demonstração"""

    VIDEO_FORMATS = ['MP4', 'MOV', 'AVI', 'MKV', 'WEBM']
    RESOLUTIONS = ['1920x1080', '1280x720', '3840x2160', '2560x1440']
    CODECS = ['H.264', 'H.265', 'VP9', 'AV1']
    FPS_OPTIONS = [24, 30, 60]

    VIDEO_TITLES = [
        "Tutorial de Python para Iniciantes",
        "Review do Novo iPhone",
        "Como Fazer Marketing Digital",
        "Análise de Dados com Pandas",
        "Entrevista com CEO Startup",
        "Podcast: Tecnologia e Inovação",
        "Webinar: IA Generativa",
        "Aula de Machine Learning",
        "Vlog: Dia de Trabalho",
        "Apresentação de Produto"
    ]

    TAGS = [
        'tutorial', 'review', 'entrevista', 'podcast', 'webinar',
        'aula', 'vlog', 'apresentação', 'tecnologia', 'marketing',
        'educação', 'negócios', 'desenvolvimento', 'dados', 'IA'
    ]

    @staticmethod
    def generate_videos(count: int = 25) -> List[Video]:
        """Gera lista de vídeos mockados"""
        videos = []

        for i in range(count):
            created_at = fake.date_time_between(start_date='-30d', end_date='now')

            # Define status com distribuição realista
            status_weights = [0.1, 0.15, 0.65, 0.05, 0.05]
            status = random.choices(
                list(VideoStatus),
                weights=status_weights
            )[0]

            # Se concluído, tem data de processamento
            processed_at = None
            if status == VideoStatus.COMPLETED:
                processed_at = created_at + timedelta(
                    minutes=random.randint(5, 120)
                )

            # Escolhe título
            title = random.choice(MockDataGenerator.VIDEO_TITLES)
            if random.random() > 0.5:
                title = f"{title} - Parte {random.randint(1, 5)}"

            video = Video(
                id=f"vid_{i+1:03d}",
                title=title,
                filename=f"{fake.uuid4()}.{random.choice(MockDataGenerator.VIDEO_FORMATS).lower()}",
                duration=random.randint(60, 7200),  # 1min a 2h
                size_mb=round(random.uniform(50, 2000), 2),
                format=random.choice(MockDataGenerator.VIDEO_FORMATS),
                resolution=random.choice(MockDataGenerator.RESOLUTIONS),
                codec=random.choice(MockDataGenerator.CODECS),
                fps=random.choice(MockDataGenerator.FPS_OPTIONS),
                status=status,
                created_at=created_at,
                processed_at=processed_at,
                thumbnail_url=f"https://via.placeholder.com/320x180?text=Video+{i+1}" if status == VideoStatus.COMPLETED else None,
                transcription=fake.text(max_nb_chars=500) if status == VideoStatus.COMPLETED and random.random() > 0.3 else None,
                subtitle_url=f"/subtitles/vid_{i+1:03d}.srt" if status == VideoStatus.COMPLETED and random.random() > 0.5 else None,
                tags=random.sample(MockDataGenerator.TAGS, k=random.randint(2, 5))
            )
            videos.append(video)

        return videos

    @staticmethod
    def generate_tasks(videos: List[Video], tasks_per_video: int = 2) -> List[Task]:
        """Gera lista de tarefas mockadas baseadas nos vídeos"""
        tasks = []
        task_id = 1

        for video in videos:
            # Gera múltiplas tarefas por vídeo
            num_tasks = random.randint(1, tasks_per_video)

            for _ in range(num_tasks):
                task_type = random.choice(list(TaskType))

                # Status da tarefa baseado no status do vídeo
                if video.status == VideoStatus.COMPLETED:
                    task_status = VideoStatus.COMPLETED
                elif video.status == VideoStatus.PROCESSING:
                    task_status = random.choice([VideoStatus.PROCESSING, VideoStatus.QUEUED])
                else:
                    task_status = video.status

                created_at = video.created_at
                started_at = None
                completed_at = None
                progress = 0

                if task_status in [VideoStatus.PROCESSING, VideoStatus.COMPLETED]:
                    started_at = created_at + timedelta(minutes=random.randint(1, 10))
                    progress = random.randint(10, 99) if task_status == VideoStatus.PROCESSING else 100

                if task_status == VideoStatus.COMPLETED:
                    completed_at = started_at + timedelta(minutes=random.randint(5, 60))

                duration_seconds = None
                if completed_at and started_at:
                    duration_seconds = (completed_at - started_at).total_seconds()

                task = Task(
                    id=f"task_{task_id:04d}",
                    video_id=video.id,
                    video_title=video.title,
                    task_type=task_type,
                    status=task_status,
                    progress=progress,
                    created_at=created_at,
                    started_at=started_at,
                    completed_at=completed_at,
                    error_message="Erro ao processar arquivo" if task_status == VideoStatus.FAILED else None,
                    duration_seconds=duration_seconds,
                    output_file=f"/output/{video.id}_{task_type.value.lower()}.mp4" if task_status == VideoStatus.COMPLETED else None
                )
                tasks.append(task)
                task_id += 1

        return tasks

    @staticmethod
    def generate_metrics(days: int = 30) -> List[Metric]:
        """Gera métricas diárias dos últimos N dias"""
        metrics = []
        end_date = datetime.now()

        for i in range(days):
            date = end_date - timedelta(days=days - i - 1)

            # Métricas com tendência de crescimento
            base_videos = 5 + i * 0.3
            videos_processed = int(base_videos + random.uniform(-2, 3))

            metric = Metric(
                date=date,
                videos_processed=max(0, videos_processed),
                total_duration_hours=round(random.uniform(2, 15), 2),
                tasks_completed=max(0, videos_processed * random.randint(1, 3)),
                tasks_failed=random.randint(0, 2),
                storage_used_gb=round(50 + i * 1.5 + random.uniform(-5, 5), 2),
                avg_processing_time_min=round(random.uniform(5, 45), 2)
            )
            metrics.append(metric)

        return metrics

    @staticmethod
    def videos_to_dataframe(videos: List[Video]) -> pd.DataFrame:
        """Converte lista de vídeos para DataFrame"""
        data = []
        for v in videos:
            data.append({
                'ID': v.id,
                'Título': v.title,
                'Arquivo': v.filename,
                'Duração (min)': round(v.duration / 60, 1),
                'Tamanho (MB)': v.size_mb,
                'Formato': v.format,
                'Resolução': v.resolution,
                'Codec': v.codec,
                'FPS': v.fps,
                'Status': v.status.value,
                'Criado em': v.created_at,
                'Processado em': v.processed_at,
                'Tags': ', '.join(v.tags)
            })
        return pd.DataFrame(data)

    @staticmethod
    def tasks_to_dataframe(tasks: List[Task]) -> pd.DataFrame:
        """Converte lista de tarefas para DataFrame"""
        data = []
        for t in tasks:
            data.append({
                'ID': t.id,
                'Vídeo': t.video_title,
                'Tipo': t.task_type.value,
                'Status': t.status.value,
                'Progresso': f"{t.progress}%",
                'Criado em': t.created_at,
                'Iniciado em': t.started_at,
                'Concluído em': t.completed_at,
                'Duração (min)': round(t.duration_seconds / 60, 1) if t.duration_seconds else None,
                'Erro': t.error_message
            })
        return pd.DataFrame(data)

    @staticmethod
    def metrics_to_dataframe(metrics: List[Metric]) -> pd.DataFrame:
        """Converte lista de métricas para DataFrame"""
        data = []
        for m in metrics:
            data.append({
                'Data': m.date.date(),
                'Vídeos Processados': m.videos_processed,
                'Duração Total (h)': m.total_duration_hours,
                'Tarefas Concluídas': m.tasks_completed,
                'Tarefas Falhadas': m.tasks_failed,
                'Armazenamento (GB)': m.storage_used_gb,
                'Tempo Médio (min)': m.avg_processing_time_min
            })
        return pd.DataFrame(data)


# Instância global para reutilização
_generator = MockDataGenerator()

def get_mock_videos(count: int = 25) -> List[Video]:
    """Obtém vídeos mockados"""
    return _generator.generate_videos(count)

def get_mock_tasks(videos: List[Video] = None) -> List[Task]:
    """Obtém tarefas mockadas"""
    if videos is None:
        videos = get_mock_videos()
    return _generator.generate_tasks(videos)

def get_mock_metrics(days: int = 30) -> List[Metric]:
    """Obtém métricas mockadas"""
    return _generator.generate_metrics(days)
