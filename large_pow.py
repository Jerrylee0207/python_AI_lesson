def large_pow(n:int, pow:int, mod:int)->int:
    if(pow==0):
        return 1;
    else:
        ans = large_pow(n, pow//2, mod)%mod;
        ans **= 2;
        ans %= mod;
        if(pow%2==1):
            ans *= n;
            ans %= mod;
        return ans;