import pytest

    @pytest.mark.asyncio
async def test_read_root(async_client):
    # Teste a rota "/"
    response = await async_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

