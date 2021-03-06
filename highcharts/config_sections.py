'''Config sections for a chart.'''
import options
from common import *


class ChartConfig(ConfigSection):
    '''
    The 'chart' section of a Highcharts config.

    See http://www.highcharts.com/ref/#chart for available options.
    '''
    defaults = {}
    available_options = options.CHART_CONFIG


class CreditsConfig(ConfigSection):
    '''
    The 'credits' section of a Highcharts config.

    See http://www.highcharts.com/ref/#credits for available options.
    '''
    defaults = {}
    available_options = options.CREDITS_CONFIG


class TitleConfig(ConfigSection):
    '''
    The 'title' section of a Highcharts config.

    See http://www.highcharts.com/ref/#title for available options.
    '''
    defaults = {}
    available_options = options.TITLE_CONFIG


class SubtitleConfig(ConfigSection):
    '''
    The 'subtitle' section of a Highcharts config.

    See http://www.highcharts.com/ref/#title for available options.
    '''
    defaults = {}
    available_options = options.SUBTITLE_CONFIG


class LegendConfig(ConfigSection):
    '''
    The 'legend' section of a Highcharts config.

    See http://www.highcharts.com/ref/#legend for available options.
    '''
    defaults = {}
    available_options = options.LEGEND_CONFIG


class TooltipConfig(ConfigSection):
    '''
    The 'tooltip' section of a Highcharts config.

    See http://www.highcharts.com/ref/#tooltip for available options.
    '''
    defaults = {}
    available_options = options.TOOLTIP_CONFIG


class XAxisConfig(ConfigSection):
    '''
    The 'xAxis' section of a Highcharts config.

    See http://www.highcharts.com/ref/#xAxis for available options.
    '''
    available_options = options.X_AXIS_CONFIG
    defaults = {
        "title": TitleConfig,
        "minTickInterval": 1,
        "tickInterval": 1,
        "tickWidth": 0.5,
        "tickLength": 10,
        "categories": []
    }


class YAxisConfig(ConfigSection):
    '''
    The 'yAxis' section of a Highcharts config.

    See http://www.highcharts.com/ref/#yAxis for available options.
    '''
    available_options = options.Y_AXIS_CONFIG
    defaults = {
        "title": TitleConfig,
    }



class plotOptionsConfig(ConfigSection):
    '''
    The 'yAxis' section of a Highcharts config.

    See http://www.highcharts.com/ref/#yAxis for available options.
    See http://api.highcharts.com/highcharts#plotOptions.line
    '''
    available_options = [] #options.Y_AXIS_CONFIG
    defaults = {
        "line": {},
        "series": {
                "lineWidth": 1,
                "dashStyle": 'Solid',
                }
    }
