---
records:
    - id: KQ5JKGTAN5
      kind: monograph
      title: Brownian Motion and Stochastic Calculus
      creators:
        - name: Ioannis Karatzas
          role: author
        - name: Steven E. Shreve
          role: author
      date: "1988"
      msc:
        - code: 60Hxx
          from: zbmath_search
        - code: 60J65
          from: zbmath_search
        - code: 60-02
          from: zbmath_search
        - code: 60J55
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1988"
          ids:
            doi:
                - 10.1007/978-1-4612-0949-2
                - 10.1007/978-1-4684-0302-2
            zbl: "0638.60065"
            zbl_id: "192908"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1998"
              ids:
                isbn:
                    - "9780387976556"
                    - "9781461209492"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer US
              date: "1988"
              ids:
                isbn:
                    - "9781468403046"
                    - "9781468403022"
              access:
                class: record
      relations:
        - kind: part_of
          to: 7ME1ABA6H5
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4612-0949-2
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4684-0302-2
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "192908"
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
