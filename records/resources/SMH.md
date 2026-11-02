---
records:
    - id: SMHP24D74F
      kind: monograph
      title: From Real to Complex Analysis
      creators:
        - name: R. H. Dyer
          role: author
        - name: D. E. Edmunds
          role: author
      date: "2014"
      msc:
        - code: 00A35
          from: zbmath_search
        - code: 97I10
          from: zbmath_search
        - code: 26-01
          from: zbmath_search
        - code: 30-01
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2014"
          ids:
            doi: 10.1007/978-3-319-06209-9
            zbl: "1296.00021"
            zbl_id: "6292869"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer International Publishing
              date: "2014"
              ids:
                isbn:
                    - "9783319062082"
                    - "9783319062099"
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
          native_id: 10.1007/978-3-319-06209-9
          level: work
        - source: zbmath_search
          snapshot: blake3:25dd7c4358839cf7c8c9f5d07f0562e94f38728153e7db2255a7191282b967c2
          native_id: "6292869"
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
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
---
