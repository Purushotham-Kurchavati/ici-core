"""
Exception hierarchy for the ICI framework.

This module defines the base exception types for all components, providing
a structured hierarchy for error handling and recovery.
"""


class ICIError(Exception):
    """Base exception for all ICI-related errors."""

    pass


# Ingestion Pipeline Errors


class IngestionError(ICIError):
    """Base exception for all ingestion-related errors."""

    pass


class IngestorError(IngestionError):
    """Base exception for all ingestor-related errors."""

    pass


class APIAuthenticationError(IngestorError):
    """Raised when API authentication fails."""

    pass


class APIRateLimitError(IngestorError):
    """Raised when API rate limits are exceeded."""

    pass


class DataFetchError(IngestorError):
    """Raised when data fetching fails."""

    pass


class PreprocessorError(IngestionError):
    """Raised when preprocessing fails."""

    pass


class IngestionPipelineError(IngestionError):
    """Raised when the ingestion pipeline encounters an error."""

    pass


# Query Pipeline Errors


class QueryError(ICIError):
    """Base exception for all query-related errors."""

    pass


class ValidationError(QueryError):
    """Raised when input validation fails."""

    pass


class EmbeddingError(ICIError):
    """Raised when embedding generation fails."""

    pass


class VectorStoreError(ICIError):
    """Base exception for all vector store related errors."""

    pass


class PromptBuilderError(QueryError):
    """Raised when prompt construction fails."""

    pass


class GenerationError(QueryError):
    """Raised when text generation fails."""

    pass


class OrchestratorError(QueryError):
    """Raised when the orchestrator encounters an error."""

    pass


# Other Errors


class ConfigurationError(ICIError):
    """Raised when configuration is invalid."""

    pass


class LoggerError(ICIError):
    """Raised when logging encounters an error."""

    pass


# Exporting all exception types
__all__ = [
    "ICIError",
    "IngestionError",
    "IngestorError",
    "APIAuthenticationError",
    "APIRateLimitError",
    "DataFetchError",
    "PreprocessorError",
    "IngestionPipelineError",
    "QueryError",
    "ValidationError",
    "EmbeddingError",
    "VectorStoreError",
    "PromptBuilderError",
    "GenerationError",
    "OrchestratorError",
    "ConfigurationError",
    "LoggerError",
]
