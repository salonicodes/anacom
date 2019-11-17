from anacom import *

#unit step signal
t=symbols('t')
##us=anacom.unitstep(t)

#diracdelta
##dd=anacom.diracdelta(t)


#signum
##sg=anacom.signum(t)


#sawtooth
##saw=anacom.sawtooth(t)

#ramp
##rp=anacom.ramp(t)

#pdf from cdf
##x=symbols('x')
##probdensity=(x-5)
##cumulativedensity=anacom.pdf(probdensity,x)

#fourier transform
##G=anacom.fTrans(us,t)
##G1=anacom.fTrans(dd,t)

#value of fourier transform
##Gval=anacom.fTransVal(G,pi)


#inverse fourier
##f=symbols('f')
##fT=1
##invF=anacom.invfTrans(1,f)
##invFval=anacom.invfTransVal(anacom.invfTrans(anacom.fTrans(us,t),f),t,0)

#Amplitude Modulation
##mt,ct=symbols('mt ct')
##mt=sin(t)
####ka=0.5
##ct=cos(t)
##modulatedWave=anacom.ampmod(mt,ka,ct)
##plot(mt)

#---------------------------------------
#Amplitude Modulation and Demodulation using np
##t=np.linspace(0,100,1000)
##em=5*np.cos(2*np.pi*50*t)
##mod_index=1/10
##ec=10*np.cos(2*np.pi*200*t)
##response_characterstic=50*np.pi*2
##lpf=np.exp(-t*response_characterstic)
##z=anacom.ampmodd(em,mod_index,ec)
##s=anacom.demodd(z,ec,lpf)

#DSBSC Modulation
##t=np.linspace(0,1,1000)
##mt=5*np.cos(2*np.pi*50*t)
##ct=10*np.cos(2*np.pi*1000000*t)
##dsbcmodulated=anacom.dsbscmod(mt,ct)

#SSBSC Modulation
##ssbsc=anacom.ssbscmod(5,5,10,10)

#Frequency Modulation
##freqMod=anacom.fremod(5,10,1,5,1)

#Phase Modulation
##phasewave=anacom.PhaseMod(5,0.3,mt,t)

#PWM
##pulsewidth=anacom.pwm(mt,t)

#PAM
##percent=40.0
##TimePeriod=10.0
##Cycles=30
##dt=0.01
##t=np.arange(0,Cycles*TimePeriod,dt);
##pwm= (t%TimePeriod) < (TimePeriod*percent/100)
##x=np.linspace(-10,10,len(pwm))
##y=(np.cos(x))
##anacom.pamd(pwm,y,t)

