from dataclasses import dataclass, asdict


@dataclass
class UploadLinkRequest:
    path: str
    overwrite: str = "true"

    def to_params(self) -> dict:
        return asdict(self)


@dataclass
class CopyResourceRequest:
    path: str
    overwrite: str = "false"

    def to_params(self, from_path: str) -> dict:
        params = asdict(self)
        params["from"] = from_path
        return params


@dataclass
class DownloadLinkRequest:
    path: str

    def to_params(self) -> dict:
        return asdict(self)


@dataclass
class CreateFolderRequest:
    path: str

    def to_params(self) -> dict:
        return asdict(self)


@dataclass
class DeleteResourceRequest:
    path: str
    permanently: bool = False

    def to_params(self) -> dict:
        params = asdict(self)
        params["permanently"] = str(self.permanently).lower()
        return params


@dataclass
class UploadResponse:
    href: str
    method: str
    templated: bool

    @classmethod
    def from_dict(cls, data: dict) -> "UploadResponse":
        return cls(
            href=data["href"],
            method=data["method"],
            templated=data.get("templated", False),
        )


@dataclass
class ResourceResponse:
    href: str
    method: str
    templated: bool

    @classmethod
    def from_dict(cls, data: dict) -> "ResourceResponse":
        return cls(
            href=data["href"],
            method=data["method"],
            templated=data.get("templated", False),
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
