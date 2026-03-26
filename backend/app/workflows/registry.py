# workflows/registry.py

class DummyWorkflow:
    def run(self, input_data: dict):
        return {"message": "dummy response", "input": input_data}


class WorkflowRegistry:
    def __init__(self):
        self._workflows = {
            "test": DummyWorkflow()
        }

    def get(self, name: str):
        return self._workflows.get(name)

    def list_workflows(self):
        return list(self._workflows.keys())


workflow_registry = WorkflowRegistry()