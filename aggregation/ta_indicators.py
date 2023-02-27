# https://awesomeopensource.com/projects/technical-analysis

import talib
import numpy as np
import pandas as pd


# TODO: comb this over remove unnessicary stuff and make sure its consistant


# returns a bunch of volume, volitiliy, monentum and other timeseries indicators using just ta libaray (not ta-lib)
# input timestamp (str), open high low close (float)
def ta_indicators(df):
    df = dropna(df)
    indicators_df = ta.add_all_ta_features(df, open="open", high="high", low="low", close="close", volume="volume", fillna=True)
    print(indicators_df)
    indicators_df.to_csv('test.csv')
    return indicators_df


# Overlap Studies Functions
def overlap_studies(df):
    upperband, middleband, lowerband = talib.BBANDS(df.Close.values, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)
    DEMA = talib.DEMA(df.Close.values, timeperiod=30)
    EMA = talib.EMA(df.Close.values, timeperiod=30)
    HT_TRENDLINE = talib.HT_TRENDLINE(df.Close.values)
    KAMA = talib.KAMA(df.Close.values, timeperiod=30)
    MA = talib.MA(df.Close.values, timeperiod=30, matype=0)
    # mama, fama = talib.MAMA(df.Close.values, fastlimit=0, slowlimit=0)
    # MAVP = talib.MAVP(df.Close.values, periods=20, minperiod=2, maxperiod=30, matype=0)
    MIDPOINT = talib.MIDPOINT(df.Close.values, timeperiod=14)
    MIDPRICE = talib.MIDPRICE(df.High.values, df.Low.values, timeperiod=14)
    SAR = talib.SAR(df.High.values, df.Low.values, acceleration=0, maximum=0)
    SAREXT = talib.SAREXT(df.High.values, df.Low.values, startvalue=0, offsetonreverse=0, accelerationinitlong=0, accelerationlong=0, accelerationmaxlong=0, accelerationinitshort=0, accelerationshort=0, accelerationmaxshort=0)
    SMA = talib.SMA(df.Close.values, timeperiod=30)
    T3 = talib.T3(df.Close.values, timeperiod=5, vfactor=0)
    TEMA = talib.TEMA(df.Close.values, timeperiod=30)
    TRIMA = talib.TRIMA(df.Close.values, timeperiod=30)
    WMA = talib.WMA(df.Close.values, timeperiod=30)

    data_df = pd.DataFrame()

    data_df['upperband'] = upperband
    data_df['middleband'] = middleband
    data_df['lowerband'] = lowerband
    data_df['DEMA'] = DEMA
    data_df['EMA'] = EMA
    data_df['HT_TRENDLINE'] = HT_TRENDLINE
    data_df['KAMA'] = KAMA
    data_df['MA'] = MA
        # data_df['mama'] = mama
        # data_df['fama'] = fama
        # data_df['MAVP'] = MAVP
    data_df['MIDPOINT'] = MIDPOINT
    data_df['MIDPRICE'] = MIDPRICE
    data_df['SAR'] = SAR
    data_df['SAREXT'] = SAREXT
    data_df['SMA'] = SMA
    data_df['T3'] = T3
    data_df['TEMA'] = TEMA
    data_df['TRIMA'] = TRIMA
    data_df['WMA'] = WMA

    result_df = data_df.iloc[-1:]

    return result_df


# TODO: What is this for? remove this??
def ohlcv_df(op, hi, lo, cl):
    data_df = pd.DataFrame()
    data_df['open'] = op
    data_df['high'] = hi
    data_df['low'] = lo
    data_df['close'] = cl
    result_df = data_df.iloc[-1:]

    return result_df


# Momentum Indicator Functions
def momentum_indicator(df):
    ADX = talib.ADX(df.High.values, df.Low.values, df.Close.values, timeperiod=14)
    ADXR = talib.ADXR(df.High.values, df.Low.values, df.Close.values, timeperiod=14)
    APO = talib.APO(df.Close.values, fastperiod=12, slowperiod=26, matype=0)
    aroondown, aroonup = talib.AROON(df.High.values, df.Low.values, timeperiod=14)
    AROONOSC = talib.AROONOSC(df.High.values, df.Low.values, timeperiod=14)
    BOP = talib.BOP(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CCI = talib.CCI(df.High.values, df.Low.values, df.Close.values, timeperiod=14)
    CMO = talib.CMO(df.Close.values, timeperiod=14)
    DX = talib.DX(df.High.values, df.Low.values, df.Close.values, timeperiod=14)
    macd, macdsignal, macdhist = talib.MACD(df.Close.values, fastperiod=12, slowperiod=26, signalperiod=9)
    macdext, macdsignalext, macdhistext = talib.MACDEXT(df.Close.values, fastperiod=12, fastmatype=0, slowperiod=26, slowmatype=0, signalperiod=9, signalmatype=0)
    macdfix, macdsignalfix, macdhistfix = talib.MACDFIX(df.Close.values, signalperiod=9)
    MFI = talib.MFI(df.High.values, df.Low.values, df.Close.values, vl, timeperiod=14)
    MINUS_DI = talib.MINUS_DI(df.High.values, df.Low.values, df.Close.values, timeperiod=14)
    MINUS_DM = talib.MINUS_DM(df.High.values, df.Low.values, timeperiod=14)
    MOM = talib.MOM(df.Close.values, timeperiod=10)
    PLUS_DI = talib.PLUS_DI(df.High.values, df.Low.values, df.Close.values, timeperiod=14)
    PLUS_DM = talib.PLUS_DM(df.High.values, df.Low.values, timeperiod=14)
    PPO = talib.PPO(df.Close.values, fastperiod=12, slowperiod=26, matype=0)
    ROC = talib.ROC(df.Close.values, timeperiod=10)
    ROCP = talib.ROCP(df.Close.values, timeperiod=10)
    ROCR = talib.ROCR(df.Close.values, timeperiod=10)
    ROCR100 = talib.ROCR100(df.Close.values, timeperiod=10)
    RSI = talib.RSI(df.Close.values, timeperiod=14)
    slowk, slowd = talib.STOCH(df.High.values, df.Low.values, df.Close.values, fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
    fastkf, fastdf = talib.STOCHF(df.High.values, df.Low.values, df.Close.values, fastk_period=5, fastd_period=3, fastd_matype=0)
    fastkrsi, fastdrsi = talib.STOCHRSI(df.Close.values, timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0)
    TRIX = talib.TRIX(df.Close.values, timeperiod=30)
    ULTOSC = talib.ULTOSC(df.High.values, df.Low.values, df.Close.values, timeperiod1=7, timeperiod2=14, timeperiod3=28)
    WILLR = talib.WILLR(df.High.values, df.Low.values, df.Close.values, timeperiod=14)

    data_df = pd.DataFrame()

    data_df['ADX'] = ADX
    data_df['ADXR'] = ADXR
    data_df['APO'] = APO
    data_df['aroondown'] = aroondown
    data_df['aroonup'] = aroonup
    data_df['AROONOSC'] = AROONOSC
    data_df['BOP'] = BOP
    data_df['CCI'] = CCI
    data_df['CMO'] = CMO
    data_df['DX'] = DX
    data_df['macd'] = macd
    data_df['macdsignal'] = macdsignal
    data_df['macdhist'] = macdhist
    data_df['macdext'] = macdext
    data_df['macdsignalext'] = macdsignalext
    data_df['macdhistext'] = macdhistext
    data_df['macdfix'] = macdfix
    data_df['macdsignalfix'] = macdsignalfix
    data_df['macdhistfix'] = macdhistfix
    data_df['MFI'] = MFI
    data_df['MINUS_DI'] = MINUS_DI
    data_df['MINUS_DM'] = MINUS_DM
    data_df['MOM'] = MOM
    data_df['PLUS_DI'] = PLUS_DI
    data_df['PLUS_DM'] = PLUS_DM
    data_df['PPO'] = PPO
    data_df['ROC'] = ROC
    data_df['ROCP'] = ROCP
    data_df['ROCR'] = ROCR
    data_df['ROCR100'] = ROCR100
    data_df['RSI'] = RSI
    data_df['slok'] = slowk
    data_df['slod'] = slowd
    data_df['fastkf'] = fastkf
    data_df['fastdf'] = fastdf
    data_df['fastkrsi'] = fastkrsi
    data_df['fastdrsi'] = fastdrsi
    data_df['TRIX'] = TRIX
    data_df['ULTOSC'] = ULTOSC
    data_df['WILLR'] = WILLR

    result_df = data_df.iloc[-1:]

    return result_df


# Volume Indicator Functions
def volume_indicators(df):
    AD = talib.AD(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    ADOSC = talib.ADOSC(df.High.values, df.Low.values, df.Close.values, df.Volume.values, fastperiod=3, slowperiod=10)
    OBV = talib.OBV(df.Close.values, df.Volume.values)

    data_df = pd.DataFrame()

    data_df['AD'] = AD
    data_df['ADOSC'] = ADOSC
    data_df['OBV'] = OBV
    result_df = data_df.iloc[-1:]
    return result_df


# Price Transform Functions
def price_transform(df):
    AVGPRICE = talib.AVGPRICE(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    MEDPRICE = talib.MEDPRICE(df.High.values, df.Low.values)
    TYPPRICE = talib.TYPPRICE(df.High.values, df.Low.values, df.Close.values)
    WCLPRICE = talib.WCLPRICE(df.High.values, df.Low.values, df.Close.values)

    data_df = pd.DataFrame()

    data_df['AVGPRICE'] = AVGPRICE
    data_df['MEDPRICE'] = MEDPRICE
    data_df['TYPPRICE'] = TYPPRICE
    data_df['WCLPRICE'] = WCLPRICE
    result_df = data_df.iloc[-1:]
    return result_df


# Cycle Indicator Functions
def cycle_indicator(df):
    HT_DCPERIOD = talib.HT_DCPERIOD(df.Close.values)
    HT_DCPHASE = talib.HT_DCPHASE(df.Close.values)
    inphase, quadrature = talib.HT_PHASOR(df.Close.values)
    sine, leadsine = talib.HT_SINE(df.Close.values)
    HT_TRENDMODE = talib.HT_TRENDMODE(df.Close.values)

    data_df = pd.DataFrame()

    data_df['HT_DCPERIOD'] = HT_DCPERIOD
    data_df['HT_DCPHASE'] = HT_DCPHASE
    data_df['inphase'] = inphase
    data_df['quadrature'] = quadrature
    data_df['sine'] = sine
    data_df['leadsine'] = leadsine
    data_df['HT_TRENDMODE'] = HT_TRENDMODE
    result_df = data_df.iloc[-1:]
    return result_df


# Pattern Recognition Functions
# Need to take a dataframe that has Open, High, Low, and Close values
def candle_pattern_recognition(df):

    CDL2CROWS = talib.CDL2CROWS(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDL3BLACKCROWS = talib.CDL3BLACKCROWS(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDL3INSIDE = talib.CDL3INSIDE(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDL3LINESTRIKE = talib.CDL3LINESTRIKE(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDL3OUTSIDE = talib.CDL3OUTSIDE(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDL3STARSINSOUTH = talib.CDL3STARSINSOUTH(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDL3WHITESOLDIERS = talib.CDL3WHITESOLDIERS(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDLABANDONEDBABY = talib.CDLABANDONEDBABY(df.Open.values, df.High.values, df.Low.values, df.Close.values, penetration=0) #TODO: find what these penetration values mean??
    CDLADVANCEBLOCK = talib.CDLADVANCEBLOCK(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDLBELTHOLD = talib.CDLBELTHOLD(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDLBREAKAWAY = talib.CDLBREAKAWAY(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDLCLOSINGMARUBOZU = talib.CDLCLOSINGMARUBOZU(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDLCONCEALBABYSWALL = talib.CDLCONCEALBABYSWALL(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDLCOUNTERATTACK = talib.CDLCOUNTERATTACK(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDLDARKCLOUDCOVER = talib.CDLDARKCLOUDCOVER(df.Open.values, df.High.values, df.Low.values, df.Close.values, penetration=0)
    CDLDOJI = talib.CDLDOJI(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDLDOJISTAR = talib.CDLDOJISTAR(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDLDRAGONFLYDOJI = talib.CDLDRAGONFLYDOJI(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDLENGULFING = talib.CDLENGULFING(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDLEVENINGDOJISTAR = talib.CDLEVENINGDOJISTAR(df.Open.values, df.High.values, df.Low.values, df.Close.values, penetration=0)
    CDLEVENINGSTAR = talib.CDLEVENINGSTAR(df.Open.values, df.High.values, df.Low.values, df.Close.values, penetration=0)
    CDLGAPSIDESIDEWHITE = talib.CDLGAPSIDESIDEWHITE(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDLGRAVESTONEDOJI = talib.CDLGRAVESTONEDOJI(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDLHAMMER = talib.CDLHAMMER(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDLHANGINGMAN = talib.CDLHANGINGMAN(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDLHARAMI = talib.CDLHARAMI(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDLHARAMICROSS = talib.CDLHARAMICROSS(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDLhiWAVE = talib.CDLHIGHWAVE(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDLHIKKAKE = talib.CDLHIKKAKE(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDLHIKKAKEMOD = talib.CDLHIKKAKEMOD(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDLHOMINGPIGEON = talib.CDLHOMINGPIGEON(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDLIDENTICAL3CROWS = talib.CDLIDENTICAL3CROWS(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDLINNECK = talib.CDLINNECK(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDLINVERTEDHAMMER = talib.CDLINVERTEDHAMMER(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDLKICKING = talib.CDLKICKING(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDLKICKINGBYLENGTH = talib.CDLKICKINGBYLENGTH(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDLLADDERBOTTOM = talib.CDLLADDERBOTTOM(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDLLONGLEGGEDDOJI = talib.CDLLONGLEGGEDDOJI(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDLLONGLINE = talib.CDLLONGLINE(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDLMARUBOZU = talib.CDLMARUBOZU(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDLMATCHINGlo = talib.CDLMATCHINGLOW(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDLMATHOLD = talib.CDLMATHOLD(df.Open.values, df.High.values, df.Low.values, df.Close.values, penetration=0)
    CDLMORNINGDOJISTAR = talib.CDLMORNINGDOJISTAR(df.Open.values, df.High.values, df.Low.values, df.Close.values, penetration=0)
    CDLMORNINGSTAR = talib.CDLMORNINGSTAR(df.Open.values, df.High.values, df.Low.values, df.Close.values, penetration=0)
    CDLONNECK = talib.CDLONNECK(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDLPIERCING = talib.CDLPIERCING(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDLRICKSHAWMAN = talib.CDLRICKSHAWMAN(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDLRISEFALL3METHODS = talib.CDLRISEFALL3METHODS(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDLSEPARATINGLINES = talib.CDLSEPARATINGLINES(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDLSHOOTINGSTAR = talib.CDLSHOOTINGSTAR(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDLSHORTLINE = talib.CDLSHORTLINE(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDLSPINNINGTOP = talib.CDLSPINNINGTOP(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDLSTALLEDPATTERN = talib.CDLSTALLEDPATTERN(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDLSTICKSANDWICH = talib.CDLSTICKSANDWICH(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDLTAKURI = talib.CDLTAKURI(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDLTASUKIGAP = talib.CDLTASUKIGAP(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDLTHRUSTING = talib.CDLTHRUSTING(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDLTRISTAR = talib.CDLTRISTAR(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDLUNIQUE3RIVER = talib.CDLUNIQUE3RIVER(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDLUPSIDEGAP2CROWS = talib.CDLUPSIDEGAP2CROWS(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    CDLXSIDEGAP3METHODS = talib.CDLXSIDEGAP3METHODS(df.Open.values, df.High.values, df.Low.values, df.Close.values)

    data_df = pd.DataFrame()
    

    # data_df['Date'] = df.Date.values
    data_df['CDL2CROWS'] = CDL2CROWS
    data_df['CDL3BLACKCROWS'] = CDL3BLACKCROWS
    data_df['CDL3INSIDE'] = CDL3INSIDE
    data_df['CDL3LINESTRIKE'] = CDL3LINESTRIKE
    data_df['CDL3OUTSIDE'] = CDL3OUTSIDE
    data_df['CDL3STARSINSOUTH'] = CDL3STARSINSOUTH
    data_df['CDL3WHITESOLDIERS'] = CDL3WHITESOLDIERS
    data_df['CDLABANDONEDBABY'] = CDLABANDONEDBABY
    data_df['CDLADVANCEBLOCK'] = CDLADVANCEBLOCK
    data_df['CDLBELTHOLD'] = CDLBELTHOLD
    data_df['CDLBREAKAWAY'] = CDLBREAKAWAY
    data_df['CDLCLOSINGMARUBOZU'] = CDLCLOSINGMARUBOZU
    data_df['CDLCONCEALBABYSWALL'] = CDLCONCEALBABYSWALL
    data_df['CDLCOUNTERATTACK'] = CDLCOUNTERATTACK
    data_df['CDLDARKCLOUDCOVER'] = CDLDARKCLOUDCOVER
    data_df['CDLDOJI'] = CDLDOJI
    data_df['CDLDOJISTAR'] = CDLDOJISTAR
    data_df['CDLDRAGONFLYDOJI'] = CDLDRAGONFLYDOJI
    data_df['CDLENGULFING'] = CDLENGULFING
    data_df['CDLEVENINGDOJISTAR'] = CDLEVENINGDOJISTAR
    data_df['CDLEVENINGSTAR'] = CDLEVENINGSTAR
    data_df['CDLGAPSIDESIDEWHITE'] = CDLGAPSIDESIDEWHITE
    data_df['CDLGRAVESTONEDOJI'] = CDLGRAVESTONEDOJI
    data_df['CDLHAMMER'] = CDLHAMMER
    data_df['CDLHANGINGMAN'] = CDLHANGINGMAN
    data_df['CDLHARAMI'] = CDLHARAMI
    data_df['CDLHARAMICROSS'] = CDLHARAMICROSS
    data_df['CDLhiWAVE'] = CDLhiWAVE
    data_df['CDLHIKKAKE'] = CDLHIKKAKE
    data_df['CDLHIKKAKEMOD'] = CDLHIKKAKEMOD
    data_df['CDLHOMINGPIGEON'] = CDLHOMINGPIGEON
    data_df['CDLIDENTICAL3CROWS'] = CDLIDENTICAL3CROWS
    data_df['CDLINNECK'] = CDLINNECK
    data_df['CDLINVERTEDHAMMER'] = CDLINVERTEDHAMMER
    data_df['CDLKICKING'] = CDLKICKING
    data_df['CDLKICKINGBYLENGTH'] = CDLKICKINGBYLENGTH
    data_df['CDLLADDERBOTTOM'] = CDLLADDERBOTTOM
    data_df['CDLLONGLEGGEDDOJI'] = CDLLONGLEGGEDDOJI
    data_df['CDLLONGLINE'] = CDLLONGLINE
    data_df['CDLMARUBOZU'] = CDLMARUBOZU
    data_df['CDLMATCHINGlo'] = CDLMATCHINGlo
    data_df['CDLMATHOLD'] = CDLMATHOLD
    data_df['CDLMORNINGDOJISTAR'] = CDLMORNINGDOJISTAR
    data_df['CDLMORNINGSTAR'] = CDLMORNINGSTAR
    data_df['CDLONNECK'] = CDLONNECK
    data_df['CDLPIERCING'] = CDLPIERCING
    data_df['CDLRICKSHAWMAN'] = CDLRICKSHAWMAN
    data_df['CDLRISEFALL3METHODS'] = CDLRISEFALL3METHODS
    data_df['CDLSEPARATINGLINES'] = CDLSEPARATINGLINES
    data_df['CDLSHOOTINGSTAR'] = CDLSHOOTINGSTAR
    data_df['CDLSHORTLINE'] = CDLSHORTLINE
    data_df['CDLSPINNINGTOP'] = CDLSPINNINGTOP
    data_df['CDLSTALLEDPATTERN'] = CDLSTALLEDPATTERN
    data_df['CDLSTICKSANDWICH'] = CDLSTICKSANDWICH
    data_df['CDLTAKURI'] = CDLTAKURI
    data_df['CDLTASUKIGAP'] = CDLTASUKIGAP
    data_df['CDLTHRUSTING'] = CDLTHRUSTING
    data_df['CDLTRISTAR'] = CDLTRISTAR
    data_df['CDLUNIQUE3RIVER'] = CDLUNIQUE3RIVER
    data_df['CDLUPSIDEGAP2CROWS'] = CDLUPSIDEGAP2CROWS
    data_df['CDLXSIDEGAP3METHODS'] = CDLXSIDEGAP3METHODS

    return data_df


def backtest_pattern_recognition(df):
    data_df = pd.DataFrame()

    # CDL2CROWS = talib.CDL2CROWS(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    # data_df['CDL2CROWS'] = CDL2CROWS

    # CDLSHOOTINGSTAR = talib.CDLSHOOTINGSTAR(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    # data_df['CDLSHOOTINGSTAR'] = CDLSHOOTINGSTAR

    CDLHAMMER = talib.CDLHAMMER(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    data_df['CDLHAMMER'] = CDLHAMMER

    CDLINVERTEDHAMMER = talib.CDLINVERTEDHAMMER(df.Open.values, df.High.values, df.Low.values, df.Close.values)
    data_df['CDLINVERTEDHAMMER'] = CDLINVERTEDHAMMER

    return data_df


# Statistic Functions
def statistic_functions(df):
    BETA = talib.BETA(df.High.values, df.Low.values, timeperiod=5)
    CORREL = talib.CORREL(df.High.values, df.Low.values, timeperiod=30)
    LINEARREG = talib.LINEARREG(df.Close.values, timeperiod=14)
    LINEARREG_ANGLE = talib.LINEARREG_ANGLE(df.Close.values, timeperiod=14)
    LINEARREG_INTERCEPT = talib.LINEARREG_INTERCEPT(df.Close.values, timeperiod=14)
    LINEARREG_SLOPE = talib.LINEARREG_SLOPE(df.Close.values, timeperiod=14)
    STDDEV = talib.STDDEV(df.Close.values, timeperiod=5, nbdev=1)
    TSF = talib.TSF(df.Close.values, timeperiod=14)
    VAR = talib.VAR(df.Close.values, timeperiod=5, nbdev=1)

    data_df = pd.DataFrame()

    data_df['BETA'] = BETA
    data_df['CORREL'] = CORREL
    data_df['LINEARREG'] = LINEARREG
    data_df['LINEARREG_ANGLE'] = LINEARREG_ANGLE
    data_df['LINEARREG_INTERCEPT'] = LINEARREG_INTERCEPT
    data_df['LINEARREG_SLOPE'] = LINEARREG_SLOPE
    data_df['STDDEV'] = STDDEV
    data_df['TSF'] = TSF
    data_df['VAR'] = VAR

    # result_df = data_df.iloc[-1:] # TODO Why did i do this?
    # return result_df

    return data_df




# Math Transform Functions
def math_transform(df):
    ACOS = talib.ACOS(df.Close.values)
    ASIN = talib.ASIN(df.Close.values)
    ATAN = talib.ATAN(df.Close.values)
    CEIL = talib.CEIL(df.Close.values)
    COS = talib.COS(df.Close.values)
    COSH = talib.COSH(df.Close.values)
    EXP = talib.EXP(df.Close.values)
    FLOOR = talib.FLOOR(df.Close.values)
    LN = talib.LN(df.Close.values)
    LOG10 = talib.LOG10(df.Close.values)
    SIN = talib.SIN(df.Close.values)
    SINH = talib.SINH(df.Close.values)
    SQRT = talib.SQRT(df.Close.values)
    TAN = talib.TAN(df.Close.values)
    TANH = talib.TANH(df.Close.values)

    data_df = pd.DataFrame()

    data_df['ACOS'] = ACOS
    data_df['ASIN'] = ASIN
    data_df['ATAN'] = ATAN
    data_df['CEIL'] = CEIL
    data_df['COS'] = COS
    data_df['COSH'] = COSH
    data_df['EXP'] = EXP
    data_df['FLOOR'] = FLOOR
    data_df['LN'] = LN
    data_df['LOG10'] = LOG10
    data_df['SIN'] = SIN
    data_df['SINH'] = SINH
    data_df['SQRT'] = SQRT
    data_df['TAN'] = TAN
    data_df['TANH'] = TANH

    result_df = data_df.iloc[-1:]
    return result_df


# Math Operator Functions
def math_operator(df):
    ADD = talib.ADD(df.High.values, lo)
    DIV = talib.DIV(df.High.values, lo)
    MAX = talib.MAX(df.Close.values, timeperiod=30)
    MAXINDEX = talib.MAXINDEX(df.Close.values, timeperiod=30)
    MIN = talib.MIN(df.Close.values, timeperiod=30)
    MININDEX = talib.MININDEX(df.Close.values, timeperiod=30)
    min, max = talib.MINMAX(df.Close.values, timeperiod=30)
    minidx, maxidx = talib.MINMAXINDEX(df.Close.values, timeperiod=30)
    MULT = talib.MULT(df.High.values, lo)
    SUB = talib.SUB(df.High.values, lo)
    SUM = talib.SUM(df.Close.values, timeperiod=30)

    data_df = pd.DataFrame()

    data_df['ADD'] = ADD
    data_df['DIV'] = DIV
    data_df['MAX'] = MAX
    data_df['MAXINDEX'] = MAXINDEX
    data_df['MIN'] = MIN
    data_df['MININDEX'] = MININDEX
    data_df['min'] = min
    data_df['max'] = max
    data_df['minidx'] = minidx
    data_df['maxidx'] = maxidx
    data_df['MULT'] = MULT
    data_df['SUB'] = SUB
    data_df['SUM'] = SUM

    result_df = data_df.iloc[-1:]
    return result_df



# TODO: Probably yeet this too? Or is good to have this one function call to do all the calls?

def make_talib_data(df):
    ohlcv = ohlcv_df(df)
    overlap_df = overlap_studies(df)
    momentum_df = momentum_indicator(df)
    volume_df = volume_indicators(dfl)
    price_df = price_transform(df)
    cycle_df = cycle_indicator(df)
    pattern_df = candle_pattern_recognition(df)
    statistic_df = statistic_functions(df)
    # math_t_df = math_transform(df)
    math_o_df = math_operator(df)

    indicator_df = pd.concat([ohlcv, overlap_df, momentum_df, volume_df, price_df, cycle_df, pattern_df, statistic_df, math_o_df], axis=1)
    return indicator_df


