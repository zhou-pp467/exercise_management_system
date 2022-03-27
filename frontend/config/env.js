const configs = {
    //测试环境
    test: {
        API_SERVER: "http://498168a75f.qicp.vip"
    },
    //开发环境
    development: {
        API_SERVER: "http://498168a75f.qicp.vip"
    },
    //本地
    local: {
        API_SERVER: "http://498168a75f.qicp.vip"
    },
    //线上
    production: {
        API_SERVER: "http://www.aryazdp.cn"
    }

}
console.log(configs[process.env.NODE_ENV].API_SERVER, "API_SERVER")

export default configs