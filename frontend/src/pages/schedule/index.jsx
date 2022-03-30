import { GridContent } from '@ant-design/pro-layout';
import zh_CN from 'antd/lib/locale-provider/zh_CN';
import CalendarEvt from './components/CalendarEvt';
import { ConfigProvider } from 'antd'
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
