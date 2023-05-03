# GET routes
@app.get('/users/{id}', response_model=schemas.UserOut)
def get_user(id: UUID, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User {id} was not found"
        )

    return user


# POST routes
@app.post('/users', status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(new_user: schemas.UserBase, db: Session = Depends(get_db)):
    hashed_psw = utils.hash(new_user.password)
    new_user.password = hashed_psw

    created_user = models.User(**new_user.dict())
    db.add(created_user)
    db.commit()
    db.refresh(created_user)
    return created_user