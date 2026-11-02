---
records:
    - id: WAM1DCZASH
      kind: monograph
      title: Introduction to Uncertainty Quantification
      creators:
        - name: T.J. Sullivan
          role: author
      date: "2015"
      msc:
        - code: 60-02
          from: zbmath_search
        - code: "60E15"
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2015"
          ids:
            doi: 10.1007/978-3-319-23395-6
            zbl: "1336.60002"
            zbl_id: "6482154"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer International Publishing
              date: "2015"
              ids:
                isbn:
                    - "9783319233949"
                    - "9783319233956"
              access:
                class: record
      relations:
        - kind: part_of
          to: 7B8JKAVW9F
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 dev scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-319-23395-6
          level: work
        - source: zbmath_search
          snapshot: blake3:25dd7c4358839cf7c8c9f5d07f0562e94f38728153e7db2255a7191282b967c2
          native_id: "6482154"
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
