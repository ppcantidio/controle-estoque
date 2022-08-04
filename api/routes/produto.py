from fastapi import APIRouter, Request

from core.models.produto import ProdutoCriar, ProdutoEditar, ProdutoConsultar
from core.service.produto import ProdutoService


router = APIRouter(
    prefix='/produtos',
    tags=['Produtos'],
)


@router.post('/')
async def criar_produto(produto: ProdutoCriar, request: Request):
    nm_id_sessao = request.headers.get('nm_id_sessao')
    nm_id_transacao = request.headers.get('nm_id_transacao')

    await ProdutoService(nm_id_sessao, nm_id_transacao).criar_produto(produto)

    return produto


@router.post('/')
async def editar_produto(produto: ProdutoEditar):
    pass


@router.post('/')
async def consultar_produto(produto: ProdutoConsultar):
    pass
