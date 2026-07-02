from dataclasses import dataclass


@dataclass
class UploadResponse:
    method: str
    href: str
    templated: bool

    @classmethod
    def from_dict(cls, data: dict) -> "UploadResponse":
        return cls(
            method=data["method"],
            href=data["href"],
            templated=data["templated"]
        )


@dataclass
class ResourceResponse:
    method: str
    href: str
    templated: bool

    @classmethod
    def from_dict(cls, data: dict) -> "ResourceResponse":
        return cls(
            method=data["method"],
            href=data["href"],
            templated=data["templated"]
        )


@dataclass
class ErrorResponse:
    error: str
    description: str
    message: str

    @classmethod
    def from_dict(cls, data: dict) -> "ErrorResponse":
        return cls(
            error=data.get("error", ""),
            description=data.get("description", ""),
            message=data.get("message", ""),
        )
