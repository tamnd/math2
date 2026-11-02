---
records:
    - id: SQE5YKVE3T
      kind: problem-set
      title: IMO 1959
      creators:
        - name: IMO Problem Selection Committee
          role: author
      date: "1959"
      msc:
        - code: 00A07
          from: imo
        - code: 97U40
          from: imo
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1959"
      relations:
        - kind: part_of
          to: 931689K6X2
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 dev scope/1
      catalogue:
        - source: imo
          snapshot: blake3:c564548c1a7c5bfe4e71cf81d61c599a9d4016d698feff8fb0bc9beb0e2f88f9
          native_id: "1959"
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
    - id: SQEFHDXMH9
      kind: monograph
      title: An Introduction to Game-Theoretic Modelling
      creators:
        - name: Mike Mesterton-Gibbons
          role: author
      date: "2000-10-13"
      msc:
        - code: 91-01
          from: zbmath_search
        - code: 91A40
          from: zbmath_search
        - code: 91A05
          from: zbmath_search
        - code: 91A10
          from: zbmath_search
        - code: 91A12
          from: zbmath_search
        - code: 91A22
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2000-10-13"
          ids:
            doi: 10.1090/stml/011
            zbl: "0967.91002"
            zbl_id: "1534336"
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "2000-10-13"
              ids:
                isbn:
                    - "9781470421281"
                    - "9780821872765"
                    - "9780821891865"
                    - "9780821819296"
              access:
                class: record
      relations:
        - kind: part_of
          to: 6RX4VMGQKK
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 dev scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/stml/011
          level: work
        - source: crossref_language
          snapshot: blake3:99510ada1a0f54f83dbf4ed97ef48852461d1f98d338d1a350cabf222fb85948
          native_id: 10.1090/stml/011
          level: work
        - source: zbmath_search
          snapshot: blake3:25dd7c4358839cf7c8c9f5d07f0562e94f38728153e7db2255a7191282b967c2
          native_id: "1534336"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
---
