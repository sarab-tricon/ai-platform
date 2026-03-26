import logging
from app.workflows.registry import workflow_registry

logger = logging.getLogger(__name__)


class ExecutionService:

    def run_agent(self, agent_name: str, input_data: dict) -> dict:
        logger.info(f"Starting execution for agent: {agent_name}")

        # 1. Get workflow
        workflow = workflow_registry.get(agent_name)

        if not workflow:
            logger.error(f"Workflow not found: {agent_name}")
            raise ValueError(f"Workflow '{agent_name}' not found")

        # 2. Execute workflow
        try:
            result = workflow.run(input_data)
            logger.info(f"Execution successful for agent: {agent_name}")
        except Exception as e:
            logger.exception("Workflow execution failed")
            raise RuntimeError(f"Execution failed: {str(e)}")

        # 3. Return response
        return {
            "status": "success",
            "data": result
        }


execution_service = ExecutionService()