REM  *****  BASIC  *****

Sub test1()
    
    print ACT(0, 2, 1)
    print ACTsig(-1, 1)
    print ACTDig(2)
    print ACTLin(2, 2.5)
End Sub

Function ACTDig(inp)	
	if (inp<=0) then 
		ACTDig=0
	else
		ACTDig=1
	end if
end Function

Function ACTLin(inp, temp)
rem t	m
rem 0,01	5
rem 0,05	3,8
rem 0,08	2,77
rem 0,1	2,31
rem 0,5	0,5
rem 0,8	0,31
rem 1	0,25
rem 1,5	0,16
rem 2	0,12
rem 2,5	0,09

	m=0.247*(temp ^ -0.806)
	v=m*inp+0.5
	
	if (v<=0) then 
		ACTLin=0
	else
		if (v>1) then 
			ACTLin=1
		else
			ACTLin = m
		end if
	end if
end Function


Function ACTSig(inp, temp)
	e=2.7
	if (inp<-1e8) then
			ACTSig = 0
	else
		if (inp>1e8) then
			ACTSig = 1
		else
			ACTSig = 1/(1+(e ^ (-inp/temp)))
		end if
	end if
		
	
End Function

Function ACT(sw, inp, temp)
	ACT = inp
	if (sw=1) then
		ACT = ACTDig(inp)
	end if
	if (sw=2) then
		ACT = ACTsig(inp, temp)
	end if
	if (sw=3) then
		ACT = ACTLin(inp, temp)
	end if
End Function

