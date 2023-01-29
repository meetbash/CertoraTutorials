methods {
    getContractAddress() returns address envfree
    getToken0DepositAddress() returns address envfree
    getToken1DepositAddress() returns address envfree
    token0Balance(address) returns uint256 envfree
    token1Balance(address) returns uint256 envfree
    owner() returns address envfree
    token0Amount() returns uint256 envfree
    token1Amount() returns uint256 envfree
    K() returns uint256 envfree
}

invariant distinctTokens()
    getToken0DepositAddress() != getToken1DepositAddress()

rule addLiqDecreasesBalanceIncreasesLPForUser(env e, address user) {

    require (user == owner());
    init_pool(e);

    uint256 token0Amt = token0Amount();
    uint256 token1Amt = token1Amount();

    uint256 balanceToken0Before = token0Balance(user);
    uint256 balanceToken1Before = token1Balance(user);
    
    add_liquidity(e);
    
    uint256 balanceToken0After = token0Balance(user);
    uint256 balanceToken1After = token1Balance(user);

    assert (balanceToken0Before >= balanceToken0After && balanceToken1Before >= balanceToken1After), "user's token balance increased after add_liq()";
}

