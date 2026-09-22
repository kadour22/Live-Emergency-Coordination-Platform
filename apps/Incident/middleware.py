import time
from django.utils import timezone


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.perf_counter()

        response = self.get_response(request)

        duration = time.perf_counter() - start_time

        timestamp = timezone.localtime().strftime("%Y-%m-%d %H:%M:%S")

        print(
            f"[{timestamp}] "
            f"{request.method} {request.get_full_path()} "
            f"-> {response.status_code} "
            f"({duration * 1000:.2f} ms)"
        )

        return response