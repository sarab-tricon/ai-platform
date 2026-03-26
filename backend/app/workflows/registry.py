import importlib, pkgutil, inspect, logging
import app.workflows.agents as agents_pkg
from app.workflows.base_workflow import BaseWorkflow

logger = logging.getLogger(__name__)

class WorkflowRegistry:
    def __init__(self):
        self._workflows = {}
        self._autodiscover()

    def _autodiscover(self):
        for _, module_name, _ in pkgutil.iter_modules(agents_pkg.__path__):
            module = importlib.import_module(f"app.workflows.agents.{module_name}")
            for _, cls in inspect.getmembers(module, inspect.isclass):
                if issubclass(cls, BaseWorkflow) and cls is not BaseWorkflow and hasattr(cls, "name"):
                    self._workflows[cls.name] = cls()
                    logger.info(f"Workflow registered: {cls.name}")

    def get(self, name: str):
        return self._workflows.get(name)

    def list_workflows(self):
        return list(self._workflows.keys())

workflow_registry = WorkflowRegistry()