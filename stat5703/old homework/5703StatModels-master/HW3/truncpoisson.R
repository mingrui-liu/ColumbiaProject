truncpoisson <- function()
  {
    
   h.function <- function(x) {
     res <- x
     index <- x < 5
     a <- 0.58178587
     b <- 0.04364283
     res[index] <- (1 + a * x + b * x^2)[index]
     res
   }

   hinv.function <- function(x) {
     res <- x
     index <- x < 5
     a <- 0.58178587
     b <- 0.04364283
     res[index] <- (( - a + sqrt(a^2 + 4 * b * (x - 1)))/(2 *b))[index]
     res
   }

   hderiv.function <- function(x)
     {
       (1-exp(-x)-x*exp(-x))/(1 - exp(- x))^2  
     }

   hderiv2.function <- function(x)
     {
       (exp( - x) * ((x - 2) * (1 - exp( - x)) + 2 * x * exp( - x)))/(1 - exp(- x))^3 
     }

    linkfun <- function(mu) {log(hinv.function(mu))}
    linkinv <- function(eta) {h.function(exp(eta))}
    variance <- function(mu) {mu*(1+hinv.function(mu)-mu)}
    validmu <- function(mu) {all(mu>0)}

   # This are squared residuals = deviance components.
   # Note that in Barry & Welsh (2002), - deviance is given.
    dev.resids <- function(y,mu,wt){-2*wt* ( y * log(hinv.function(mu)) - hinv.function(mu) - log(1 -exp( - hinv.function(mu))) + ifelse(y==1,0, - y * log(hinv.function(y)) + hinv.function(y) + log(1 - exp( - hinv.function(y)))))}

    # It is in fact -2 loglik  
    aic <- function(y,n,mu,wt,dev){-2*sum(log(dpois(y,mu)/(1-exp(-mu)))*wt)}
    
    mu.eta <- function(eta) {hderiv.function(exp(eta))*exp(eta)}

    dvar <- function(mu)
       {
         (1+hinv.function(mu)-mu) + mu*(1/hderiv.function(hinv.function(mu))-1)
       }
   
    d2link <- function(mu)
      {
        -1/(hinv.function(mu))^2/(hderiv.function(hinv.function(mu)))^2 - 1/hinv.function(mu)/(hderiv.function(hinv.function(mu)))^3*hderiv2.function(hinv.function(mu))
      }

    initialize <- expression({
      mustart <- y
      mustart[mustart==1] <- 1.1})    

    structure(list(family="truncpoisson",link="trunclog",linkfun=linkfun,linkinv=linkinv,variance=variance,dev.resids=dev.resids,aic=aic,mu.eta=mu.eta,dvar=dvar,d2link=d2link,initialize=initialize,validmu=validmu),class="family")
  }

