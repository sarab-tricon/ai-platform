from db.models import Execution
from repositories.base import BaseRepository


class ExecutionRepository(BaseRepository):

    def create_execution(self, workflow_id: int):
        execution = Execution(workflow_id=workflow_id, status="pending")
        self.db.add(execution)
        self.db.commit()
        self.db.refresh(execution)
        return execution

    def update_status(self, execution_id: int, status: str, result: str = None):
        execution = self.db.query(Execution).filter(Execution.id == execution_id).first()
        if execution:
            execution.status = status
            execution.result = result
            self.db.commit()
            self.db.refresh(execution)
        return execution