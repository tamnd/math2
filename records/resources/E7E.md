---
records:
    - id: E7EP34FVMZ
      kind: monograph
      title: Elements of Abstract Analysis
      creators:
        - name: Mícheál Ó Searcóid
          role: author
      date: "2002"
      msc:
        - code: 00A05
          from: zbmath_search
        - code: 46-01
          from: zbmath_search
        - code: 54-01
          from: zbmath_search
        - code: 26-01
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2002"
          ids:
            doi: 10.1007/978-1-4471-0179-6
            zbl: "0999.00002"
            zbl_id: "1676799"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer London
              date: "2002"
              ids:
                isbn:
                    - "9781852334246"
                    - "9781447101796"
              access:
                class: record
      relations:
        - kind: part_of
          to: 3YXAC8SZBF
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 dev scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4471-0179-6
          level: work
        - source: zbmath_search
          snapshot: blake3:25dd7c4358839cf7c8c9f5d07f0562e94f38728153e7db2255a7191282b967c2
          native_id: "1676799"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
        - op: scope
          at: "2026-11-02"
          by: m2 v0.6.17 scope/1
          note: from in to in
---
