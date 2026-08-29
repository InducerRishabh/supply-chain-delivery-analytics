SELECT
    "Days for shipment (scheduled)" AS scheduled_shipping_days,

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
        AVG("Days for shipping (real)"),
        2
    ) AS avg_actual_shipping_days,

    ROUND(
        AVG(
            "Days for shipping (real)"
            - "Days for shipment (scheduled)"
        ),
        2
    ) AS avg_shipping_delay_days

FROM read_csv_auto(
    'data/DataCoSupplyChain_UTF8.csv'
)

WHERE "Delivery Status" IN (
    'Advance shipping',
    'Late delivery',
    'Shipping on time'
)

GROUP BY
    "Days for shipment (scheduled)"

ORDER BY
    scheduled_shipping_days;