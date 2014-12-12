from __future__ import absolute_import

from .base import Result, ResultError, ResultParseError
from .dns import DnsResult
from .http import HttpResult
from .ping import PingResult
from .ssl import SslResult
from .traceroute import TracerouteResult
from .ntp import NtpResult

__version__ = "0.5.1"

__all__ = (
    "Result",
    "PingResult",
    "TracerouteResult",
    "DnsResult",
    "SslResult",
    "HttpResult",
    "NtpResult",
    "version",
)
