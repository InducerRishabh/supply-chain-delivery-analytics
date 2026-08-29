SELECT
    "Category Name" AS category,

    COUNT(*) AS delivery_records,

    SUM(
        CASE
            WHEN "Delivery Status" = 'Late delivery'
            THEN 1
            ELSE 0
        END
    ) AS late_deliveries,

    ROUND(
        100.0 * SUM(
            CASE
                WHEN "Delivery Status" = 'Late delivery'
                THEN 1
                ELSE 0
            END
        ) / COUNT(*),
        2
    ) AS late_delivery_rate_pct,

    ROUND(
        AVG(
            "Days for shipping (real)"
            - "Days for shipment (scheduled)"
        ),
        2
    ) AS avg_shipping_delay_days,

    ROUND(
        SUM("Sales"),
        2
    ) AS total_sales

FROM read_csv_auto(
    'data/DataCoSupplyChain_UTF8.csv'
)

WHERE "Delivery Status" IN (
    'Advance shipping',
    'Late delivery',
    'Shipping on time'
)

GROUP BY
    "Category Name"

ORDER BY
    late_deliveries DESC;