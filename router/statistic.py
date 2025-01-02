from fastapi import APIRouter, Depends, HTTPException, status
from db.schemas import constructionDisplay, LFDisplay, ConditionDisplay, processingDisplay, documentDisplay, statusDisplay, HanhChinhDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db import construction, livestock, product, legal_docs,statisticals
from typing import List
from db import huyen_xa_moi


router = APIRouter(
    prefix="/statistic",
    tags=["statistic"]
)

@router.get("/water_retail/", response_model=List[constructionDisplay])
async def all_constructions(db: Session = Depends(get_db)):
    try:
        constructions = construction.get_all_retail(db=db)
        return [constructionDisplay.from_orm(Construction) for Construction in constructions]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        
@router.get("/water_focus/", response_model=List[constructionDisplay])
async def all_focus_constructions(db: Session = Depends(get_db)):
    try:
        constructions = construction.get_all_focus(db=db)
        return [constructionDisplay.from_orm(Construction) for Construction in constructions]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/farm_with_condition/", response_model=List[ConditionDisplay])
async def all_farm(db: Session = Depends(get_db)):
    try:
        farms = livestock.get_farm_with_condition(db=db)
        return [ConditionDisplay.from_orm(Farm) for Farm in farms]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# @router.get("/processing/", response_model=List[processingDisplay])
# async def all_processing(db: Session = Depends(get_db)):
#     try:
#         processings = product.list_facilities(db=db)
#         return [processingDisplay.from_orm(Processing) for Processing in processings]
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
    
# @router.get("/documents/", response_model=List[documentDisplay])
# async def all_document(db: Session = Depends(get_db)):
#     try:
#         documents = legal_docs.list_documents(db=db)   
#         return [documentDisplay.from_orm(Document) for Document in documents]
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/history_access/", response_model=List[statusDisplay])
async def all_history_access(db: Session = Depends(get_db)):
    try:
        status = statisticals.list_status(db=db)
        return [statusDisplay.from_orm(Status) for Status in status]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/huyen/", response_model=List[HanhChinhDisplay]) 
async def all_huyen(db: Session = Depends(get_db)):
    try:
        huyen = huyen_xa_moi.list_huyen(db=db)
        return [HanhChinhDisplay.from_orm(Huyen) for Huyen in huyen]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))  
    
@router.get("/xa/", response_model=List[HanhChinhDisplay])
async def all_xa(db: Session = Depends(get_db)):
    try:
        xa = huyen_xa_moi.list_xa(db=db)
        return [HanhChinhDisplay.from_orm(Xa) for Xa in xa]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))     