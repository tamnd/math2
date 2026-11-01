---
records:
    - id: 1GNB9J7ZWE
      kind: monograph
      title: 'Real Analysis: Foundations and Functions of One Variable'
      creators:
        - name: Miklós Laczkovich
          role: author
        - name: Vera T. Sós
          role: author
      date: "2015"
      msc:
        - code: 26-01
          from: zbmath_search
        - code: 26Axx
          from: zbmath_search
        - code: 00A06
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2015"
          ids:
            doi:
                - 10.1007/978-1-4939-2766-1
                - 10.1007/978-1-4939-7369-9
            zbl: "1325.26001"
            zbl_id: "6432575"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2015"
              ids:
                isbn:
                    - "9781493927654"
                    - "9781493927661"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer New York
              date: "2017"
              ids:
                isbn:
                    - "9781493973675"
                    - "9781493973699"
              access:
                class: record
      relations:
        - kind: part_of
          to: NWQC4TW7S9
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4939-2766-1
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4939-7369-9
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "6432575"
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
