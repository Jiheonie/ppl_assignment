# Generated from d:/hoc_ki_231/ppl/ass3/assignment3/initial/src/main/CSlang/parser/CSlang.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *


def serializedATN():
    return [
        4,0,61,459,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,
        65,7,65,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,
        1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,
        1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,15,
        1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,
        1,18,1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,20,1,20,
        1,21,1,21,1,22,1,22,1,23,1,23,1,24,1,24,1,25,1,25,1,25,1,26,1,26,
        1,26,1,27,1,27,1,27,1,28,1,28,1,28,1,29,1,29,1,30,1,30,1,30,1,31,
        1,31,1,32,1,32,1,32,1,33,1,33,1,34,1,34,1,34,1,35,1,35,1,36,1,36,
        1,37,1,37,1,38,1,38,1,39,1,39,1,40,1,40,1,41,1,41,1,42,1,42,1,43,
        1,43,1,44,1,44,1,45,1,45,1,46,1,46,1,47,1,47,1,48,1,48,1,48,1,49,
        1,49,1,49,1,49,1,49,3,49,315,8,49,1,49,1,49,3,49,319,8,49,1,50,1,
        50,5,50,323,8,50,10,50,12,50,326,9,50,1,51,1,51,3,51,330,8,51,1,
        51,1,51,1,52,4,52,335,8,52,11,52,12,52,336,1,52,1,52,1,53,1,53,1,
        53,5,53,344,8,53,10,53,12,53,347,9,53,1,53,1,53,1,53,1,54,3,54,353,
        8,54,1,54,1,54,1,55,1,55,1,55,1,55,1,55,1,55,1,55,1,55,1,55,1,55,
        1,55,1,55,1,55,1,55,3,55,371,8,55,1,56,1,56,1,56,1,56,1,56,1,56,
        1,56,1,56,1,56,3,56,382,8,56,1,57,1,57,5,57,386,8,57,10,57,12,57,
        389,9,57,1,58,1,58,4,58,393,8,58,11,58,12,58,394,1,59,1,59,1,60,
        1,60,1,60,1,60,5,60,403,8,60,10,60,12,60,406,9,60,1,60,1,60,1,61,
        1,61,1,61,1,61,5,61,414,8,61,10,61,12,61,417,9,61,1,61,1,61,1,61,
        1,61,1,61,1,62,4,62,425,8,62,11,62,12,62,426,1,62,1,62,1,63,1,63,
        1,63,1,63,5,63,435,8,63,10,63,12,63,438,9,63,1,63,1,63,1,63,1,64,
        1,64,1,64,5,64,446,8,64,10,64,12,64,449,9,64,1,64,1,64,3,64,453,
        8,64,1,64,1,64,1,65,1,65,1,65,2,415,447,0,66,1,1,3,2,5,3,7,4,9,5,
        11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,33,
        17,35,18,37,19,39,20,41,21,43,22,45,23,47,24,49,25,51,26,53,27,55,
        28,57,29,59,30,61,31,63,32,65,33,67,34,69,35,71,36,73,37,75,38,77,
        39,79,40,81,41,83,42,85,43,87,44,89,45,91,46,93,47,95,48,97,49,99,
        50,101,0,103,0,105,51,107,52,109,0,111,0,113,53,115,54,117,55,119,
        0,121,56,123,57,125,58,127,59,129,60,131,61,1,0,9,1,0,48,57,2,0,
        69,69,101,101,2,0,43,43,45,45,2,0,34,34,92,92,3,0,65,90,95,95,97,
        122,4,0,48,57,65,90,95,95,97,122,2,0,10,10,13,13,3,0,8,10,12,13,
        32,32,1,0,34,34,478,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,
        0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,
        0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,
        0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,
        0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,
        0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,0,
        0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,0,0,0,0,67,1,0,
        0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,0,0,0,75,1,0,0,0,0,77,1,0,
        0,0,0,79,1,0,0,0,0,81,1,0,0,0,0,83,1,0,0,0,0,85,1,0,0,0,0,87,1,0,
        0,0,0,89,1,0,0,0,0,91,1,0,0,0,0,93,1,0,0,0,0,95,1,0,0,0,0,97,1,0,
        0,0,0,99,1,0,0,0,0,105,1,0,0,0,0,107,1,0,0,0,0,113,1,0,0,0,0,115,
        1,0,0,0,0,117,1,0,0,0,0,121,1,0,0,0,0,123,1,0,0,0,0,125,1,0,0,0,
        0,127,1,0,0,0,0,129,1,0,0,0,0,131,1,0,0,0,1,133,1,0,0,0,3,135,1,
        0,0,0,5,141,1,0,0,0,7,150,1,0,0,0,9,153,1,0,0,0,11,158,1,0,0,0,13,
        162,1,0,0,0,15,166,1,0,0,0,17,172,1,0,0,0,19,177,1,0,0,0,21,184,
        1,0,0,0,23,191,1,0,0,0,25,196,1,0,0,0,27,202,1,0,0,0,29,214,1,0,
        0,0,31,218,1,0,0,0,33,223,1,0,0,0,35,227,1,0,0,0,37,232,1,0,0,0,
        39,238,1,0,0,0,41,243,1,0,0,0,43,245,1,0,0,0,45,247,1,0,0,0,47,249,
        1,0,0,0,49,251,1,0,0,0,51,253,1,0,0,0,53,256,1,0,0,0,55,259,1,0,
        0,0,57,262,1,0,0,0,59,265,1,0,0,0,61,267,1,0,0,0,63,270,1,0,0,0,
        65,272,1,0,0,0,67,275,1,0,0,0,69,277,1,0,0,0,71,280,1,0,0,0,73,282,
        1,0,0,0,75,284,1,0,0,0,77,286,1,0,0,0,79,288,1,0,0,0,81,290,1,0,
        0,0,83,292,1,0,0,0,85,294,1,0,0,0,87,296,1,0,0,0,89,298,1,0,0,0,
        91,300,1,0,0,0,93,302,1,0,0,0,95,304,1,0,0,0,97,306,1,0,0,0,99,318,
        1,0,0,0,101,320,1,0,0,0,103,327,1,0,0,0,105,334,1,0,0,0,107,340,
        1,0,0,0,109,352,1,0,0,0,111,370,1,0,0,0,113,381,1,0,0,0,115,383,
        1,0,0,0,117,390,1,0,0,0,119,396,1,0,0,0,121,398,1,0,0,0,123,409,
        1,0,0,0,125,424,1,0,0,0,127,430,1,0,0,0,129,442,1,0,0,0,131,456,
        1,0,0,0,133,134,5,92,0,0,134,2,1,0,0,0,135,136,5,98,0,0,136,137,
        5,114,0,0,137,138,5,101,0,0,138,139,5,97,0,0,139,140,5,107,0,0,140,
        4,1,0,0,0,141,142,5,99,0,0,142,143,5,111,0,0,143,144,5,110,0,0,144,
        145,5,116,0,0,145,146,5,105,0,0,146,147,5,110,0,0,147,148,5,117,
        0,0,148,149,5,101,0,0,149,6,1,0,0,0,150,151,5,105,0,0,151,152,5,
        102,0,0,152,8,1,0,0,0,153,154,5,101,0,0,154,155,5,108,0,0,155,156,
        5,115,0,0,156,157,5,101,0,0,157,10,1,0,0,0,158,159,5,102,0,0,159,
        160,5,111,0,0,160,161,5,114,0,0,161,12,1,0,0,0,162,163,5,105,0,0,
        163,164,5,110,0,0,164,165,5,116,0,0,165,14,1,0,0,0,166,167,5,102,
        0,0,167,168,5,108,0,0,168,169,5,111,0,0,169,170,5,97,0,0,170,171,
        5,116,0,0,171,16,1,0,0,0,172,173,5,98,0,0,173,174,5,111,0,0,174,
        175,5,111,0,0,175,176,5,108,0,0,176,18,1,0,0,0,177,178,5,115,0,0,
        178,179,5,116,0,0,179,180,5,114,0,0,180,181,5,105,0,0,181,182,5,
        110,0,0,182,183,5,103,0,0,183,20,1,0,0,0,184,185,5,114,0,0,185,186,
        5,101,0,0,186,187,5,116,0,0,187,188,5,117,0,0,188,189,5,114,0,0,
        189,190,5,110,0,0,190,22,1,0,0,0,191,192,5,110,0,0,192,193,5,117,
        0,0,193,194,5,108,0,0,194,195,5,108,0,0,195,24,1,0,0,0,196,197,5,
        99,0,0,197,198,5,108,0,0,198,199,5,97,0,0,199,200,5,115,0,0,200,
        201,5,115,0,0,201,26,1,0,0,0,202,203,5,99,0,0,203,204,5,111,0,0,
        204,205,5,110,0,0,205,206,5,115,0,0,206,207,5,116,0,0,207,208,5,
        114,0,0,208,209,5,117,0,0,209,210,5,99,0,0,210,211,5,116,0,0,211,
        212,5,111,0,0,212,213,5,114,0,0,213,28,1,0,0,0,214,215,5,118,0,0,
        215,216,5,97,0,0,216,217,5,114,0,0,217,30,1,0,0,0,218,219,5,115,
        0,0,219,220,5,101,0,0,220,221,5,108,0,0,221,222,5,102,0,0,222,32,
        1,0,0,0,223,224,5,110,0,0,224,225,5,101,0,0,225,226,5,119,0,0,226,
        34,1,0,0,0,227,228,5,118,0,0,228,229,5,111,0,0,229,230,5,105,0,0,
        230,231,5,100,0,0,231,36,1,0,0,0,232,233,5,99,0,0,233,234,5,111,
        0,0,234,235,5,110,0,0,235,236,5,115,0,0,236,237,5,116,0,0,237,38,
        1,0,0,0,238,239,5,102,0,0,239,240,5,117,0,0,240,241,5,110,0,0,241,
        242,5,99,0,0,242,40,1,0,0,0,243,244,5,43,0,0,244,42,1,0,0,0,245,
        246,5,45,0,0,246,44,1,0,0,0,247,248,5,42,0,0,248,46,1,0,0,0,249,
        250,5,47,0,0,250,48,1,0,0,0,251,252,5,33,0,0,252,50,1,0,0,0,253,
        254,5,38,0,0,254,255,5,38,0,0,255,52,1,0,0,0,256,257,5,124,0,0,257,
        258,5,124,0,0,258,54,1,0,0,0,259,260,5,61,0,0,260,261,5,61,0,0,261,
        56,1,0,0,0,262,263,5,58,0,0,263,264,5,61,0,0,264,58,1,0,0,0,265,
        266,5,61,0,0,266,60,1,0,0,0,267,268,5,33,0,0,268,269,5,61,0,0,269,
        62,1,0,0,0,270,271,5,60,0,0,271,64,1,0,0,0,272,273,5,60,0,0,273,
        274,5,61,0,0,274,66,1,0,0,0,275,276,5,62,0,0,276,68,1,0,0,0,277,
        278,5,62,0,0,278,279,5,61,0,0,279,70,1,0,0,0,280,281,5,94,0,0,281,
        72,1,0,0,0,282,283,5,37,0,0,283,74,1,0,0,0,284,285,5,40,0,0,285,
        76,1,0,0,0,286,287,5,41,0,0,287,78,1,0,0,0,288,289,5,91,0,0,289,
        80,1,0,0,0,290,291,5,93,0,0,291,82,1,0,0,0,292,293,5,46,0,0,293,
        84,1,0,0,0,294,295,5,44,0,0,295,86,1,0,0,0,296,297,5,58,0,0,297,
        88,1,0,0,0,298,299,5,59,0,0,299,90,1,0,0,0,300,301,5,123,0,0,301,
        92,1,0,0,0,302,303,5,125,0,0,303,94,1,0,0,0,304,305,5,34,0,0,305,
        96,1,0,0,0,306,307,5,60,0,0,307,308,5,45,0,0,308,98,1,0,0,0,309,
        310,3,105,52,0,310,311,3,101,50,0,311,319,1,0,0,0,312,314,3,105,
        52,0,313,315,3,101,50,0,314,313,1,0,0,0,314,315,1,0,0,0,315,316,
        1,0,0,0,316,317,3,103,51,0,317,319,1,0,0,0,318,309,1,0,0,0,318,312,
        1,0,0,0,319,100,1,0,0,0,320,324,3,83,41,0,321,323,7,0,0,0,322,321,
        1,0,0,0,323,326,1,0,0,0,324,322,1,0,0,0,324,325,1,0,0,0,325,102,
        1,0,0,0,326,324,1,0,0,0,327,329,7,1,0,0,328,330,7,2,0,0,329,328,
        1,0,0,0,329,330,1,0,0,0,330,331,1,0,0,0,331,332,3,105,52,0,332,104,
        1,0,0,0,333,335,7,0,0,0,334,333,1,0,0,0,335,336,1,0,0,0,336,334,
        1,0,0,0,336,337,1,0,0,0,337,338,1,0,0,0,338,339,6,52,0,0,339,106,
        1,0,0,0,340,345,3,95,47,0,341,344,8,3,0,0,342,344,3,111,55,0,343,
        341,1,0,0,0,343,342,1,0,0,0,344,347,1,0,0,0,345,343,1,0,0,0,345,
        346,1,0,0,0,346,348,1,0,0,0,347,345,1,0,0,0,348,349,3,95,47,0,349,
        350,6,53,1,0,350,108,1,0,0,0,351,353,5,13,0,0,352,351,1,0,0,0,352,
        353,1,0,0,0,353,354,1,0,0,0,354,355,5,10,0,0,355,110,1,0,0,0,356,
        357,5,92,0,0,357,371,5,98,0,0,358,359,5,92,0,0,359,371,5,102,0,0,
        360,361,5,92,0,0,361,371,5,114,0,0,362,363,5,92,0,0,363,371,5,110,
        0,0,364,365,5,92,0,0,365,371,5,116,0,0,366,367,5,92,0,0,367,371,
        5,92,0,0,368,369,5,92,0,0,369,371,5,34,0,0,370,356,1,0,0,0,370,358,
        1,0,0,0,370,360,1,0,0,0,370,362,1,0,0,0,370,364,1,0,0,0,370,366,
        1,0,0,0,370,368,1,0,0,0,371,112,1,0,0,0,372,373,5,116,0,0,373,374,
        5,114,0,0,374,375,5,117,0,0,375,382,5,101,0,0,376,377,5,102,0,0,
        377,378,5,97,0,0,378,379,5,108,0,0,379,380,5,115,0,0,380,382,5,101,
        0,0,381,372,1,0,0,0,381,376,1,0,0,0,382,114,1,0,0,0,383,387,7,4,
        0,0,384,386,3,119,59,0,385,384,1,0,0,0,386,389,1,0,0,0,387,385,1,
        0,0,0,387,388,1,0,0,0,388,116,1,0,0,0,389,387,1,0,0,0,390,392,5,
        64,0,0,391,393,3,119,59,0,392,391,1,0,0,0,393,394,1,0,0,0,394,392,
        1,0,0,0,394,395,1,0,0,0,395,118,1,0,0,0,396,397,7,5,0,0,397,120,
        1,0,0,0,398,399,5,47,0,0,399,400,5,47,0,0,400,404,1,0,0,0,401,403,
        8,6,0,0,402,401,1,0,0,0,403,406,1,0,0,0,404,402,1,0,0,0,404,405,
        1,0,0,0,405,407,1,0,0,0,406,404,1,0,0,0,407,408,6,60,2,0,408,122,
        1,0,0,0,409,410,5,47,0,0,410,411,5,42,0,0,411,415,1,0,0,0,412,414,
        9,0,0,0,413,412,1,0,0,0,414,417,1,0,0,0,415,416,1,0,0,0,415,413,
        1,0,0,0,416,418,1,0,0,0,417,415,1,0,0,0,418,419,5,42,0,0,419,420,
        5,47,0,0,420,421,1,0,0,0,421,422,6,61,2,0,422,124,1,0,0,0,423,425,
        7,7,0,0,424,423,1,0,0,0,425,426,1,0,0,0,426,424,1,0,0,0,426,427,
        1,0,0,0,427,428,1,0,0,0,428,429,6,62,2,0,429,126,1,0,0,0,430,436,
        3,95,47,0,431,435,8,8,0,0,432,433,5,92,0,0,433,435,5,34,0,0,434,
        431,1,0,0,0,434,432,1,0,0,0,435,438,1,0,0,0,436,434,1,0,0,0,436,
        437,1,0,0,0,437,439,1,0,0,0,438,436,1,0,0,0,439,440,3,95,47,0,440,
        441,6,63,3,0,441,128,1,0,0,0,442,447,3,95,47,0,443,446,8,8,0,0,444,
        446,3,111,55,0,445,443,1,0,0,0,445,444,1,0,0,0,446,449,1,0,0,0,447,
        448,1,0,0,0,447,445,1,0,0,0,448,452,1,0,0,0,449,447,1,0,0,0,450,
        453,3,109,54,0,451,453,5,0,0,1,452,450,1,0,0,0,452,451,1,0,0,0,453,
        454,1,0,0,0,454,455,6,64,4,0,455,130,1,0,0,0,456,457,9,0,0,0,457,
        458,6,65,5,0,458,132,1,0,0,0,21,0,314,318,324,329,336,343,345,352,
        370,381,387,394,404,415,426,434,436,445,447,452,6,1,52,0,1,53,1,
        6,0,0,1,63,2,1,64,3,1,65,4
    ]

class CSlangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    BREAK = 2
    CONTINUE = 3
    IF = 4
    ELSE = 5
    FOR = 6
    INT = 7
    FLOAT = 8
    BOOL = 9
    STRING = 10
    RETURN = 11
    NULL = 12
    CLASS = 13
    CONSTRUCTOR = 14
    VAR = 15
    SELF = 16
    NEW = 17
    VOID = 18
    CONST = 19
    FUNC = 20
    ADD_OP = 21
    SUB_OP = 22
    MUL_OP = 23
    DIV_OP = 24
    NOT_OP = 25
    AND_OP = 26
    OR_OP = 27
    EQUAL_OP = 28
    ASSIGN_OP = 29
    DECL_OP = 30
    DIFF_OP = 31
    LESS_OP = 32
    LESS_EQUAL_OP = 33
    GREATER_OP = 34
    GREATER_EQUAL_OP = 35
    CONCAT_OP = 36
    MOD_OP = 37
    LP = 38
    RP = 39
    LSB = 40
    RSB = 41
    DOT = 42
    COMMA = 43
    COLON = 44
    SEMICOLON = 45
    LCB = 46
    RCB = 47
    DOU_Q = 48
    INHERIT = 49
    FLOAT_LIT = 50
    INT_LIT = 51
    STR_LIT = 52
    BOOL_LIT = 53
    ID = 54
    AT_ID = 55
    CMT_LINE = 56
    CMT_BLOCK = 57
    WS = 58
    ILLEGAL_ESCAPE = 59
    UNCLOSE_STRING = 60
    ERROR_CHAR = 61

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\\'", "'break'", "'continue'", "'if'", "'else'", "'for'", 
            "'int'", "'float'", "'bool'", "'string'", "'return'", "'null'", 
            "'class'", "'constructor'", "'var'", "'self'", "'new'", "'void'", 
            "'const'", "'func'", "'+'", "'-'", "'*'", "'/'", "'!'", "'&&'", 
            "'||'", "'=='", "':='", "'='", "'!='", "'<'", "'<='", "'>'", 
            "'>='", "'^'", "'%'", "'('", "')'", "'['", "']'", "'.'", "','", 
            "':'", "';'", "'{'", "'}'", "'\"'", "'<-'" ]

    symbolicNames = [ "<INVALID>",
            "BREAK", "CONTINUE", "IF", "ELSE", "FOR", "INT", "FLOAT", "BOOL", 
            "STRING", "RETURN", "NULL", "CLASS", "CONSTRUCTOR", "VAR", "SELF", 
            "NEW", "VOID", "CONST", "FUNC", "ADD_OP", "SUB_OP", "MUL_OP", 
            "DIV_OP", "NOT_OP", "AND_OP", "OR_OP", "EQUAL_OP", "ASSIGN_OP", 
            "DECL_OP", "DIFF_OP", "LESS_OP", "LESS_EQUAL_OP", "GREATER_OP", 
            "GREATER_EQUAL_OP", "CONCAT_OP", "MOD_OP", "LP", "RP", "LSB", 
            "RSB", "DOT", "COMMA", "COLON", "SEMICOLON", "LCB", "RCB", "DOU_Q", 
            "INHERIT", "FLOAT_LIT", "INT_LIT", "STR_LIT", "BOOL_LIT", "ID", 
            "AT_ID", "CMT_LINE", "CMT_BLOCK", "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
            "ERROR_CHAR" ]

    ruleNames = [ "T__0", "BREAK", "CONTINUE", "IF", "ELSE", "FOR", "INT", 
                  "FLOAT", "BOOL", "STRING", "RETURN", "NULL", "CLASS", 
                  "CONSTRUCTOR", "VAR", "SELF", "NEW", "VOID", "CONST", 
                  "FUNC", "ADD_OP", "SUB_OP", "MUL_OP", "DIV_OP", "NOT_OP", 
                  "AND_OP", "OR_OP", "EQUAL_OP", "ASSIGN_OP", "DECL_OP", 
                  "DIFF_OP", "LESS_OP", "LESS_EQUAL_OP", "GREATER_OP", "GREATER_EQUAL_OP", 
                  "CONCAT_OP", "MOD_OP", "LP", "RP", "LSB", "RSB", "DOT", 
                  "COMMA", "COLON", "SEMICOLON", "LCB", "RCB", "DOU_Q", 
                  "INHERIT", "FLOAT_LIT", "DECPART", "EXPPART", "INT_LIT", 
                  "STR_LIT", "NEWLINE", "ESCAPE", "BOOL_LIT", "ID", "AT_ID", 
                  "SEQUENCE", "CMT_LINE", "CMT_BLOCK", "WS", "ILLEGAL_ESCAPE", 
                  "UNCLOSE_STRING", "ERROR_CHAR" ]

    grammarFileName = "CSlang.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[52] = self.INT_LIT_action 
            actions[53] = self.STR_LIT_action 
            actions[63] = self.ILLEGAL_ESCAPE_action 
            actions[64] = self.UNCLOSE_STRING_action 
            actions[65] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            	for i in self.text:
            		if i != '0' or self.text == '0':
            			break
            		self.text = self.text[1:] 

     

    def STR_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            	self.text = self.text[1:-1]

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	esc_list = ['b', 'f', 'r', 'n', 't', '"', '\\']
            	for idx in range(1, len(self.text) - 2):
            		if self.text[idx] == '\\' and self.text[idx+1] not in esc_list:
            			raise IllegalEscape(self.text[1:idx + 2]) 
            			break

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            	string_error = self.text[1:]
            	if (string_error[-1] == "\n"):
            		raise UncloseString(self.text[1:-1])
            	else:
            		raise UncloseString(self.text[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise ErrorToken(self.text)
     


