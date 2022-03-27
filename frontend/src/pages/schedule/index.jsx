import { Suspense, useEffect, useState } from 'react';
import { EllipsisOutlined, CaretLeftOutlined, CaretRightOutlined } from '@ant-design/icons';
import { Col, Dropdown, Menu, Row } from 'antd';
import { GridContent } from '@ant-design/pro-layout';
import IntroduceRow from './components/IntroduceRow';
import SalesCard from './components/SalesCard';
import TopSearch from './components/TopSearch';
import ProportionSales from './components/ProportionSales';
import OfflineData from './components/OfflineData';
import { useRequest } from 'umi';
import { getCalendarData, getDayData } from './service';
import PageLoading from './components/PageLoading';
import { getTimeDistance } from './utils/utils';
import styles from './style.less';
import { Calendar, Badge } from 'antd';
import { Modal, Button, Space } from 'antd';
import { LocaleProvider, ConfigProvider } from 'antd';
import zh_CN from 'antd/lib/locale-provider/zh_CN';
import moment from 'moment';
import CalendarEvt from './components/CalendarEvt';


const Schedule = () => {

  return (
    <GridContent>
      <ConfigProvider locale={zh_CN}>
        <CalendarEvt />
      </ConfigProvider>
    </GridContent>
  )

}


export default Schedule;
