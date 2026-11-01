---
records:
    - id: P1Y3TZ1XGY
      kind: monograph
      title: Field Arithmetic
      creators:
        - name: Michael D. Fried
          role: author
        - name: Moshe Jarden
          role: author
      date: "2008"
      msc:
        - code: "12E30"
          from: zbmath_search
        - code: 12-02
          from: zbmath_search
        - code: "12E25"
          from: zbmath_search
        - code: 12F12
          from: zbmath_search
        - code: 12Lxx
          from: zbmath_search
        - code: 14G05
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2008"
          ids:
            doi:
                - 10.1007/978-3-031-28020-7
                - 10.1007/978-3-540-77270-5
            zbl: "1145.12001"
            zbl_id: "5278962"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Nature Switzerland
              date: "2023"
              ids:
                isbn:
                    - "9783031280191"
                    - "9783031280207"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "2008"
              ids:
                isbn:
                    - "9783540772699"
                    - "9783540772705"
              access:
                class: record
      relations:
        - kind: part_of
          to: 4G0ADS0K0R
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-031-28020-7
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-540-77270-5
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "5278962"
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
