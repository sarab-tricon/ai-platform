import logging
from app.workflows.registry import workflow_registry

logger = logging.getLogger(__name__)


class WorkflowService:

    def list_workflows(self):
        logger.info("Fetching workflow list")
        return workflow_registry.list_workflows()

    def get_workflow(self, name: str):
        logger.info(f"Fetching workflow: {name}")

        workflows = workflow_registry.list_workflows()

        if name not in workflows:
            logger.error(f"Workflow not found: {name}")
            raise ValueError(f"Workflow '{name}' not found")

        return {
            "name": name
        }


workflow_service = WorkflowService()