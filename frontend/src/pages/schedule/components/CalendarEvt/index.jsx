import React, { Component } from 'react';
import FullCalendar from '@fullcalendar/react';
import dayGridPlugin from '@fullcalendar/daygrid';
import timeGridPlugin from "@fullcalendar/timegrid";
import "@fullcalendar/core/main.css";
import "@fullcalendar/daygrid/main.css";
import "@fullcalendar/timegrid/main.css";
import configs from '../../../../../config/env'
import moment from 'moment';
import axios from 'axios'
import './index.less'

const url = configs[process.env.NODE_ENV].API_SERVER

class CalendarDemo extends Component {
    constructor(props) {
        super(props);
        this.state = {

        };
        // 日历实例
        this.myRef = React.createRef();
    }

    render() {
        return (
            <div className='container'>
                <FullCalendar
                    ref={this.myRef}
                    className="#calendar-exercise"
                    defaultView="dayGridMonth"
                    plugins={[dayGridPlugin,
                        //  timeGridPlugin
                    ]}
                    header={{
                        left: "prevYear,prev,next,nextYear today", // 上一年，上一月，下一月，下一年 今天
                        center: "title", // 当前年月
                        right: "dayGridMonth,timeGridWeek,timeGridDay" // 月 周 天
                    }}
                    locale='zh-cn'
                    buttonText={{
                        today: '当月',
                        month: '月',
                        week: '周',
                        day: '天',
                        // prev: "上个月",
                        // next: "下个月",
                        // prevYear: "上年",
                        // nextYear: "下年"
                    }}
                    allDayText='全天'
                    firstDay={1}
                    slotLabelFormat={{
                        hour: '2-digit',
                        minute: '2-digit',
                        meridiem: false,
                        hour12: false
                    }}
                    eventClick={
                        arg => {
                            // 后续点击事件跳转详情，该event回调能用到
                            console.log("当前日期有日程，所以你能点击")
                        }
                    }
                    events={(arg, successCallback) => {
                        let events = []
                        //ref不能同步获取，设置timeout微任务异步执行
                        const timer = setTimeout(() => {
                            clearTimeout(timer);
                            const YM = this.myRef?.current.calendar.view.title;  //获取标题title，截取年月的数值
                            if (YM.length > 8) return
                            const ym = YM.replace('年', '-').replace('月', '');
                            const year = moment(ym).format('YYYY');
                            const month = moment(ym).format('MM');
                            axios(`${url}/get_day_data?year=${year}&month=${month}`).then(res => {
                                let { data } = res
                                if (data?.businessCode * 1 === 1000) {
                                    let { content } = data
                                    if (content?.length) {
                                        let newArray = content.map(_item => {
                                            let { type } = _item
                                            return {
                                                ..._item,
                                                repeatExecute: false, //不重复
                                                allDay: true, //整天
                                                textColor: '#fff',
                                                backgroundColor: type == "error" ? "#e38a8a" : "#008000b0",
                                                borderColor: "transparent",
                                            }
                                        })
                                        events = newArray
                                    }
                                    successCallback(events)
                                }
                            })
                        }, 0)
                    }}
                    eventTimeFormat={
                        {
                            hour: '2-digit',
                            minute: '2-digit',
                            meridiem: false,
                            hour12: false
                        }
                    }

                />
            </div>
        );
    }
}

export default CalendarDemo