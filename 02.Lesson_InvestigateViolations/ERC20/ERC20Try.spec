methods {
    balanceOf(address) returns (uint256) envfree => DISPATCHER(true);
}

invariant shouldFail(address u) 
    balanceOf(u) > 0
