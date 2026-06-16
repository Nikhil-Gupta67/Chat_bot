"""Utility functions for the chatbot"""
import hashlib
import logging
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)


def generate_session_id(user_identifier=None):
    """Generate a unique session ID"""
    if user_identifier:
        data = f"{user_identifier}_{datetime.now().isoformat()}"
    else:
        data = datetime.now().isoformat()
    return hashlib.sha256(data.encode()).hexdigest()[:16]


def get_confidence_color(confidence):
    """Get a color based on confidence score"""
    if confidence >= 0.9:
        return 'green'
    elif confidence >= 0.7:
        return 'blue'
    elif confidence >= 0.5:
        return 'orange'
    else:
        return 'red'


def format_timestamp(timestamp):
    """Format timestamp for display"""
    if isinstance(timestamp, str):
        return timestamp
    return timestamp.strftime('%Y-%m-%d %H:%M:%S')


def calculate_session_duration(start, end):
    """Calculate session duration"""
    if isinstance(start, str):
        start = datetime.fromisoformat(start)
    if isinstance(end, str):
        end = datetime.fromisoformat(end)
    
    duration = end - start
    return {
        'seconds': duration.total_seconds(),
        'minutes': duration.total_seconds() / 60,
        'formatted': str(duration).split('.')[0]
    }


def truncate_text(text, length=50):
    """Truncate text to specified length"""
    if len(text) <= length:
        return text
    return text[:length] + '...'


def get_response_quality_metrics(messages):
    """Calculate quality metrics for responses"""
    if not messages:
        return {
            'avg_confidence': 0,
            'total_messages': 0,
            'high_confidence_count': 0,
        }
    
    total = len(messages)
    confidences = [m.confidence_score for m in messages]
    avg_confidence = sum(confidences) / total
    high_confidence_count = sum(1 for c in confidences if c >= 0.8)
    
    return {
        'avg_confidence': round(avg_confidence, 2),
        'total_messages': total,
        'high_confidence_count': high_confidence_count,
        'high_confidence_percentage': round((high_confidence_count / total) * 100, 1),
    }
