###
import sys

line1 = sys.stdin.readline().strip("\n");
line2 = sys.stdin.readline().strip("\n");

lstShowInfo = line1.split();
lstSignatureShows = line2.split();

nShowCount = lstShowInfo.pop(0);
nSignatureShowCount = lstSignatureShows.pop(0);

lstSignatureShows = lstSignatureShows[::2]
nMinsOverlap = 0;

#print(lstShowInfo);
#print(lstSignatureShows);

nCurrentSigTime = nSignatureShowCount[0]
#for i in range(len(lstShowInfo)):
    



