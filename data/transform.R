przeksztalc=function(filename)
{
    S=read.csv(filename)[,2]
    n=length(S)
    X=log(S[2:n]/S[1:(n-1)])

    Q=quantile(X,seq(from=0.2,to=0.8,by=0.2))
    KWANTYLOWO=sapply(X,function(x) {B=which(x<Q)[1]; if(is.na(B)) length(Q)+1 else B})
    KWANTYLOWO=KWANTYLOWO-(max(KWANTYLOWO)+1)/2 #wysrodkowanie
    write.csv(KWANTYLOWO,file=paste(filename,"kwantylowo.csv",sep="_"))

    ODCHYLENIOWO=round((X-mean(X))/sd(X))
    write.csv(ODCHYLENIOWO,file=paste(filename,"odchyleniowo.csv",sep="_"))
}
#przeksztalc("wig_d.csv")
przeksztalc("google.csv")
przeksztalc("microsoft.csv")
przeksztalc("ibm.csv")

