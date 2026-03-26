from db.models import Workflow
from repositories.base import BaseRepository


class WorkflowRepository(BaseRepository):

    def create_workflow(self, name: str, user_id: int):
        workflow = Workflow(name=name, user_id=user_id)
        self.db.add(workflow)
        self.db.commit()
        self.db.refresh(workflow)
        return workflow

    def get_user_workflows(self, user_id: int):
        return self.db.query(Workflow).filter(Workflow.user_id == user_id).all()