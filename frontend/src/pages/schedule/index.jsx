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
import { LocaleProvider } from 'antd';
import zh_CN from 'antd/lib/locale-provider/zh_CN';
import moment from 'moment';

const headerStyle = {
  textAlign: "center",
  height: '100px',
  lineHeight: '100px',
  fontFamily: "PingFangSC-Medium",
  fontSize: 18,
  fontWeight: "500",
  display: "flex",
  alignItems: "center",
  justifyContent: 'center'
}
const textStyle = {
  paddingLeft: 20,
  paddingRight: 20
}

const DateCellRender = (props) => {
  const { value, currentYearMonth } = props
  const [node, setNode] = useState(<></>)
  useEffect(() => {
    getNode()
  }, [value])

  const getNode = async () => {
    let formatDate = value.format('YYYY-MM-DD')
    let date = value.format('MM')
    //判断当前输出月份是否与头部月份相同
    if (date == currentYearMonth.format("MM")) {
      try {
        let result = await getDayData(formatDate) || {} //调用接口
        let listData = result.content || []
        listData?.length ?
          setNode(
            <ul className="events">
              {
                listData.map(item => {
                  return (
                    <li key={item.content}>
                      <Badge status={item.type} text={item.content} />
                    </li>
                  )
                })}
            </ul>)
          : setNode(<></>)
      } catch (error) {
        setNode(<></>)
      }
    }
  }
  return node
}

function info() {
  Modal.info({
    title: '',
    content: (
      <div>
        <p>some messages...some messages...</p>
        <p>some messages...some messages...</p>
      </div>
    ),
    onOk() { },
  });
}

const Schedule = () => {
  const [currentYearMonth, setCurrentYearMonth] = useState(moment().endOf('day'));

  const headerRender = ({ value, onChange }) => {
    const handleClickMonth = (type) => {
      //左箭头往前1个月，右箭头，往后1个月
      let clickMode = type === 'prev' ? 'subtract' : 'add'
      let month = moment(currentYearMonth)[clickMode](1, "month")
      //设置当前年月份
      setCurrentYearMonth(month)
      //触发改变面板对应值的回调函数
      onChange(month)
    }


    return (
      <div className="customeHeader" style={headerStyle}>
        <Button size="small"
          shape="circle"
          icon={<CaretLeftOutlined />}
          onClick={() => { handleClickMonth('prev') }}
        />
        <span className="title" style={textStyle}>{moment(currentYearMonth).format('YYYY年MM月')}</span>
        <Button size="small"
          shape="circle"
          icon={<CaretRightOutlined />}
          onClick={() => handleClickMonth('next')}
        />
      </div>
    )
  }

  return (
    <GridContent>
      <LocaleProvider locale={zh_CN}>
        <Calendar
          dateCellRender={value => <DateCellRender value={value} currentYearMonth={currentYearMonth} />}
          headerRender={headerRender}
        />
      </LocaleProvider>
    </GridContent>
  )

}




export default Schedule;
