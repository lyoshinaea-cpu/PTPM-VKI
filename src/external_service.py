from abc import ABC, abstractmethod


class ExternalService(ABC):

    @abstractmethod
    def send_result(self, result: str) -> None:
        ...


class SimulatedExternalService(ExternalService):

    def send_result(self, result: str) -> None:
        print(f"Имитация отправки на сервер: {result}")
