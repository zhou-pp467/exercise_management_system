import { Suspense, useEffect, useState } from 'react';
import { EllipsisOutlined } from '@ant-design/icons';
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
import { LocaleProvider } from 'antd';
import zh_CN from 'antd/lib/locale-provider/zh_CN';
import moment from 'moment';

const DateCellRender = (props) => {
  const { value, dataSource } = props
  let exercise_response
  let running_response
  const [node, setNode] = useState(<></>)
  useEffect(() => {
    getNode(value)
    console.log(dataSource, value)
  }, [dataSource])
  async function getNode (v) {
    let date = v.format('YYYY-MM-DD')
    let listData = await getDayData(date) //调用接口
    exercise_response = listData.exercise_response || []
    running_response = listData.running_response || []
    // console.log(exercise_response, running_response)
    setNode(
      <ul className="events">
        {
          exercise_response ? exercise_response.map(item => {
            return (
              <li key={item.content}>
                <Badge status={item.type} text={item.content} />
              </li>
            )
          }) : null}
        {
          running_response ? running_response.map(item => (
            <li key={item.content}>
              <Badge status={item.type} text={item.content} />
            </li>
          )) : null}
      </ul>)
  }
  return node
}

function info () {
  Modal.info({
    title: '',
    content: (
      <div>
        <p>some messages...some messages...</p>
        <p>some messages...some messages...</p>
      </div>
    ),
    onOk () { },
  });
}

const Schedule = () => {
  const [dataSource, setDataSource] = useState('')


  const onPanelChange = (e) => {
    let date = e['_d']
    setDataSource(moment(date).format("yyyy-MM-DD"))
  }


  return (
    <GridContent>
      <LocaleProvider locale={zh_CN}>
        <Calendar
          dateCellRender={value => <DateCellRender value={value} dataSource={dataSource} />}
          onPanelChange={onPanelChange}
          // onSelect={info}
          headerRender={(obj) => {
            return <div style={{ paddingTop: 10, paddingBottom: 10, textAlign: 'center' }}>
              <h3><span>{ }</span>{obj.value.format('YYYY-MM-DD') + '（适合ipad或电脑上查看）'}<span>{ }</span></h3>
            </div>
          }}
        />
      </LocaleProvider>
    </GridContent>
  )
}





export default Schedule;
