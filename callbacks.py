"""
Custom Callback Handlers for LangChain Agent Monitoring

This module provides custom callback handlers for monitoring and debugging
LLM interactions in the React Agent implementation. These handlers enable
real-time visibility into prompt-response cycles and facilitate debugging
of complex RAG-based ice breaker applications.

Original work by Eden Marco (@emarco177)
Educational implementation from Eden Marco's Udemy Course on LangChain

Author: Based on Eden Marco's educational content
License: MIT
"""

from typing import TYPE_CHECKING, Any, Optional, Union
from uuid import UUID
from typing_extensions import Self
from langchain_core.callbacks import BaseCallbackHandler
from langchain_core.outputs import LLMResult


class AgentCallbackHandler(BaseCallbackHandler):
    """
    Custom callback handler for monitoring LLM interactions in ReAct agents.
    
    This handler provides real-time monitoring capabilities for LLM prompts and responses,
    enabling enhanced debugging and transparency for RAG-based ice breaker applications.
    It captures and displays both the input prompts sent to the language model and the
    corresponding responses, facilitating development and troubleshooting.
    
    The handler integrates seamlessly with LangChain's callback system and provides
    formatted output for better readability during agent execution.
    """
    def on_llm_start(
        self,
        serialized: dict[str, Any],
        prompts: list[str],
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        tags: Optional[list[str]] = None,
        metadata: Optional[dict[str, Any]] = None,
        **kwargs: Any,
    ) -> None:
        """
        Monitor and log LLM startup events.

        This method is triggered when a Language Model starts processing a request.
        It provides visibility into the prompts being sent to the LLM, which is
        crucial for debugging agent behavior and understanding the reasoning process
        in RAG-enabled ice breaker applications.

        **ATTENTION**: This method is called for non-chat models (regular LLMs). If
            you're implementing a handler for a chat model,
            you should use on_chat_model_start instead.

        Args:
            serialized (dict[str, Any]): The serialized LLM configuration.
            prompts (list[str]): The prompts being sent to the LLM.
            run_id (UUID): The unique identifier for the current run.
            parent_run_id (Optional[UUID]): The parent run identifier, if applicable.
            tags (Optional[list[str]]): Associated tags for categorization.
            metadata (Optional[dict[str, Any]]): Additional metadata.
            kwargs (Any): Additional keyword arguments.
        """
        print("🔍 " + "=" * 60)
        print("📝 PROMPT TO LLM:")
        print("🔍 " + "=" * 60)
        print(f"{prompts[0]}")
        print("🔍 " + "=" * 60)

    def on_llm_end(
        self,
        response: LLMResult,
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        tags: Optional[list[str]] = None,
        **kwargs: Any,
    ) -> None:
        """
        Monitor and log LLM completion events.

        This method is triggered when a Language Model completes processing and
        generates a response. It captures the LLM's output, providing insight into
        the reasoning and decision-making process of the agent. This is particularly
        valuable for understanding how the agent interprets tools and formulates
        responses in RAG-based ice breaker scenarios.

        Args:
            response (LLMResult): The generated response from the language model.
            run_id (UUID): The unique identifier for the current run.
            parent_run_id (Optional[UUID]): The parent run identifier, if applicable.
            tags (Optional[list[str]]): Associated tags for categorization.
            kwargs (Any): Additional keyword arguments.
        """
        print("🤖 " + "=" * 60)
        print("💬 LLM RESPONSE:")
        print("🤖 " + "=" * 60)
        print(f"{response.generations[0][0].text}")
        print("🤖 " + "=" * 60)