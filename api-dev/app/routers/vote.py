from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import schemas, db, models, oauth2
from sqlalchemy.orm import Session

router = APIRouter(prefix="/vote", tags=["Vote"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db: Session = Depends(db.get_db), curr_user: str = Depends(oauth2.get_curr_user)):
    post = db.query(models.Posts).filter(
        models.Posts.id == vote.post_id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post {vote.post_id} was not found")

    query = db.query(models.Vote).filter(models.Vote.post_id ==
                                         vote.post_id, models.Vote.user_id == curr_user.id)

    if vote.dir == 1:
        if query.first():
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail=f"User {curr_user.id} has already voted on post {vote.post_id}")
        new_vote = models.Vote(post_id=vote.post_id, user_id=curr_user.id)
        db.add(new_vote)
        db.commit()
        return {"message": "Vote added"}
    else:
        if not query.first():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Vote not found")
        query.delete(synchronize_session=False)
        db.commit()
        return {"message": "Vote deleted"}
