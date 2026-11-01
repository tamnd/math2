---
records:
    - id: BMQ5T63AJJ
      kind: monograph
      title: Motivic Integration
      creators:
        - name: Antoine Chambert-Loir
          role: author
        - name: Johannes Nicaise
          role: author
        - name: Julien Sebag
          role: author
      date: "2018"
      msc:
        - code: "14E18"
          from: zbmath_search
        - code: 14-02
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2018"
          ids:
            doi: 10.1007/978-1-4939-7887-8
            zbl: "1545.14021"
            zbl_id: "6862764"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2018"
              ids:
                isbn:
                    - "9781493978854"
                    - "9781493978878"
              access:
                class: record
      relations:
        - kind: part_of
          to: VS2PFDMCR5
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4939-7887-8
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "6862764"
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
